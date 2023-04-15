import numpy
import math
import sys
import struct
import numpy as np

'''
uint8_t  BYTE   == B
uint32_t DWORD  == I
int32_t  LONG   == i
uint16_t WORD   == H
'''

def bilinear(src_img, dst_shape):
    """
    双线性插值法,来调整图片尺寸

    :param org_img: 原始图片
    :param dst_shape: 调整后的目标图片的尺寸
    :return:    返回调整尺寸后的图片矩阵信息
    """
    dst_img = np.zeros((dst_shape[0], dst_shape[1], 3), np.uint8)
    dst_h, dst_w = dst_shape
    src_h = src_img.shape[0]
    src_w = src_img.shape[1]
    # i：纵坐标y，j：横坐标x
    # 缩放因子，dw,dh
    scale_w = src_w / dst_w
    scale_h = src_h / dst_h

    for i in range(dst_h):
        for j in range(dst_w):
            src_x = float((j + 0.5) * scale_w - 0.5)
            src_y = float((i + 0.5) * scale_h - 0.5)

            # 向下取整，代表靠近源点的左上角的那一点的行列号
            src_x_int = math.floor(src_x)
            src_y_int = math.floor(src_y)

            # 取出小数部分，用于构造权值
            src_x_float = src_x - src_x_int
            src_y_float = src_y - src_y_int

            if src_x_int + 1 == src_w or src_y_int + 1 == src_h:
                dst_img[i, j, :] = src_img[src_y_int, src_x_int, :]
                continue
            dst_img[i, j, :] = (1. - src_y_float) * (1. - src_x_float) * src_img[src_y_int, src_x_int, :] + \
                               (1. - src_y_float) * src_x_float * src_img[src_y_int, src_x_int + 1, :] + \
                               src_y_float * (1. - src_x_float) * src_img[src_y_int + 1, src_x_int, :] + \
                               src_y_float * src_x_float * src_img[src_y_int + 1, src_x_int + 1, :]
    return dst_img

if __name__=='__main__':

    class BF():
        Type=0
        Size=1
        Reserved1 = 2
        Reserved2 = 3
        OffBits = 4


    class BI():
        Size = 0
        Width = 1
        Height = 2
        Planes = 3
        BitCount = 4
        Compression = 5
        SizeImage = 6
        XPelsPerMeter = 7
        YPelsPerMeter = 8
        ClrUsed = 9
        ClrImportant = 10


    class rgbt():
        Blue = 0
        Green = 1
        Red = 2

    if len(sys.argv)!=4:
        print("Usage: ./transform infile outfile resolution")
        sys.exit(1)

    new_widhei=sys.argv[3].split('*')

    try:
        for i in range(0, len(new_widhei)):
            int(new_widhei[i])
    except:
        print("input isn't correct",file=sys.stderr)
        sys.exit(2)
    finally:
        pass

    if len(new_widhei)!=2 and new_widhei[0]!='90' and new_widhei[0]!='180' and new_widhei[0]!='270':
        print("new size isn't correct",file=sys.stderr)
        sys.exit(3)

    if len(new_widhei)==2:
        nwid = int(new_widhei[1])  # 新的宽
        nhei = int(new_widhei[0])  # 新的高

        with open(sys.argv[1],"rb") as inptr, open(sys.argv[2],"wb") as ouptr:

            ina = inptr.read(14)
            bf = struct.unpack('<HIHHI', ina)
            lst_bf = list(bf)

            inb = inptr.read(40)
            bi = struct.unpack('<IiiHHIIiiII', inb)
            lst_bi = list(bi)

            padding = int(lst_bi[BI.Width]) - 4 * ((int(lst_bi[BI.Width]) // 4)) # 原有padding
            pad =int(nwid) - 4 * ((int(nwid) // 4)) # 新padding
            if inptr==None:
                print("Could not open",file=sys.stderr)
                sys.exit(4)

            if ouptr==None:
                print("Could not create",file=sys.stderr)
                sys.exit(5)

            if lst_bf[BF.Type] != 0x4d42 or lst_bf[BF.OffBits] != 54 or lst_bi[BI.Size] != 40 or lst_bi[BI.BitCount] != 24 or lst_bi[BI.Compression] != 0:
                print("Unsupported file format.", file=sys.stderr)
                sys.exit(6)

            wid=int(lst_bi[BI.Width])
            hei=int(lst_bi[BI.Height])

            lst_bi[BI.Width]=nwid
            lst_bi[BI.Height]=nhei
            lst_bi[BI.SizeImage]=int(nhei)*(pad+int(nwid))*3
            lst_bf[BF.Size]=lst_bi[BI.SizeImage]+14+40

            outa = struct.pack('<HIHHI', *lst_bf)
            outb = struct.pack('<IiiHHIIiiII', *lst_bi)

            ouptr.write(outa)
            ouptr.write(outb)

            bas=b''
            for i in range (hei):
                hang =inptr.read(wid*3)
                inptr.seek(padding, 1)
                bas+=hang

            list_matrix = [b for b in bas]
            num_mat = numpy.array(list_matrix)
            res = num_mat.reshape(hei, wid, 3)

            idn=bilinear(res,(nhei,nwid))
            res_idn=idn.reshape(nhei,nwid*3)

            for i in range (nhei):
                ling = b'0'*pad
                for j in range(nwid*3):
                    ouptr.write(res_idn[i][j])
                ouptr.write(ling)

            print("All Folks")
            sys.exit(0)


    if len(new_widhei)!=2 and new_widhei[0]=='90':

        with open(sys.argv[1], "rb") as inptr, open(sys.argv[2], "wb") as ouptr:

            if inptr == None:
                print("Could not open", file=sys.stderr)
                sys.exit(4)

            if ouptr == None:
                print("Could not create", file=sys.stderr)
                sys.exit(5)

            ina = inptr.read(14)
            bf = struct.unpack('<HIHHI', ina)
            lst_bf = list(bf)

            inb = inptr.read(40)
            bi = struct.unpack('<IiiHHIIiiII', inb)
            lst_bi = list(bi)

            pad = int((4 - (lst_bi[BI.Width] * 3) % 4) % 4)  # 原有的padding
            # 变换长和宽
            wid = int(lst_bi[BI.Width])  # width
            hei = int(lst_bi[BI.Height])  # height
            gd = wid
            wid = hei
            hei = gd
            lst_bi[BI.Width] = wid  # width
            lst_bi[BI.Height] = hei  # height

            padding = int((4 - (lst_bi[BI.Width] * 3) % 4) % 4)  # 新的padding
            lst_bi[BI.SizeImage] = (wid + padding) * hei * 3  # sizeimage
            lst_bf[BI.Width] = 14 + 40 + lst_bi[BI.SizeImage]  # size

            outa = struct.pack('<HIHHI', *lst_bf)
            outb = struct.pack('<IiiHHIIiiII', *lst_bi)

            if bf[BF.Type] != 0x4d42 or bf[BF.OffBits] != 54 or bi[BI.Size] != 40 or bi[BI.BitCount] != 24 or bi[
                BI.Compression] != 0:
                print("Unsupported file format.", file=sys.stderr)
                sys.exit(6)

            ouptr.write(outa)
            ouptr.write(outb)

            matrix = []  # 定义一个矩阵
            for i in range(0, abs(lst_bi[BI.Height])):  # 在0到height的范围
                du = []
                for j in range(0, bi[BI.Width]):  # 在0到width的范围
                    triple = inptr.read(3)
                    du.append(triple)
                matrix.append(du)
                inptr.seek(pad, 1)

            # 左右对称
            matrix2 = []
            for j in range(bi[BI.Width]):
                lst = []
                for i in range(abs(lst_bi[BI.Height]) - 1, -1, -1):
                    lst.append(matrix[j][i])
                # print(lst)
                matrix2.append(lst)

            # 转置
            matrix3 = []
            for j in range(bi[BI.Width]):
                tran = []
                for i in range(abs(lst_bi[BI.Height])):
                    tran.append(matrix2[i][j])
                matrix3.append(tran)

            for i in range(abs(lst_bi[BI.Height])):
                ling = b'0'
                hang = b''
                for j in range(0, bi[BI.Width]):
                    ouptr.write(matrix3[i][j])
                hang += ling * padding
                ouptr.write(hang)

            print("All folks")
            sys.exit(0)


    if len(new_widhei)!=2 and new_widhei[0]=='180':
        infile = sys.argv[1]  # 原来的bmp格式图片被赋予变量名称infile
        outfile = sys.argv[2]  # 新的bmp格式图片被赋予变量名称outfile

        with open(sys.argv[1],"rb") as inptr, open(sys.argv[2],"wb") as ouptr:

            if inptr == None:
                print("Could not open", file=sys.stderr)
                sys.exit(4)

            if ouptr == None:
                print("Could not create", file=sys.stderr)
                sys.exit(5)

            ina = inptr.read(14)
            bf = struct.unpack('<HIHHI', ina)
            lst_bf = list(bf)

            inb = inptr.read(40)
            bi = struct.unpack('<IiiHHIIiiII', inb)
            lst_bi = list(bi)

            pad = (4 - (lst_bi[BI.Width] * 3) % 4) % 4  # 原有的padding

            wid = int(lst_bi[BI.Width])  # width
            hei = int(lst_bi[BI.Height])  # height

            outa = struct.pack('<HIHHI', *lst_bf)
            outb = struct.pack('<IiiHHIIiiII', *lst_bi)

            if bf[BF.Type] != 0x4d42 or bf[BF.OffBits] != 54 or bi[BI.Size] != 40 or bi[BI.BitCount] != 24 or bi[
                BI.Compression] != 0:
                print("Unsupported file format.", file=sys.stderr)
                sys.exit(6)

            ouptr.write(outa)
            ouptr.write(outb)

            matrix = []  # 定义一个矩阵
            for i in range(0, abs(lst_bi[BI.Height])):  # 在0到height的范围
                hang = []
                ling = b'0'
                for j in range(0, bi[BI.Width]):  # 在0到width的范围
                    triple = inptr.read(3)
                    hang.append(triple)
                matrix.append(hang)
                inptr.seek(pad, 1)

            matrix2 = []
            for i in range(abs(lst_bi[BI.Height]) - 1, -1, -1):
                lst = []
                for j in range(bi[BI.Width]):
                    lst.append(matrix[i][j])
                matrix2.append(lst)

            matrix3 = []
            for j in range(bi[BI.Width]):
                lst = []
                for i in range(abs(lst_bi[BI.Height]) - 1, -1, -1):
                    lst.append(matrix2[j][i])
                matrix3.append(lst)

            for i in range(abs(lst_bi[BI.Height])):
                ling = b'0'
                hang = b''
                for j in range(0, bi[BI.Width]):
                    ouptr.write(matrix3[i][j])
                hang += ling * pad
                ouptr.write(hang)

            print("All folks")
            sys.exit(0)


    if len(new_widhei) != 2 and new_widhei[0] == '270':
        infile = sys.argv[1]  # 原来的bmp格式图片被赋予变量名称infile
        outfile = sys.argv[2]  # 新的bmp格式图片被赋予变量名称outfile
        with open("what.bmp", "rb") as inptr, open("k.bmp", "wb") as ouptr:
            if inptr == None:
                print("Could not open", file=sys.stderr)
                sys.exit(4)

            if ouptr == None:
                print("Could not create", file=sys.stderr)
                sys.exit(5)

            ina = inptr.read(14)
            bf = struct.unpack('<HIHHI', ina)
            lst_bf = list(bf)

            inb = inptr.read(40)
            bi = struct.unpack('<IiiHHIIiiII', inb)
            lst_bi = list(bi)

            pad = int((4 - (lst_bi[BI.Width] * 3) % 4) % 4)  # 原有的padding
            # 变换长和宽
            wid = int(lst_bi[BI.Width])  # width
            hei = int(lst_bi[BI.Height])  # height
            gd = wid
            wid = hei
            hei = gd
            lst_bi[BI.Width] = wid  # width
            lst_bi[BI.Height] = hei  # height

            padding = int((4 - (lst_bi[BI.Width] * 3) % 4) % 4)  # 新的padding
            lst_bi[BI.SizeImage] = (wid + padding) * hei * 3  # sizeimage
            lst_bf[BI.Width] = 14 + 40 + lst_bi[BI.SizeImage]  # size

            outa = struct.pack('<HIHHI', *lst_bf)
            outb = struct.pack('<IiiHHIIiiII', *lst_bi)

            if bf[BF.Type] != 0x4d42 or bf[BF.OffBits] != 54 or bi[BI.Size] != 40 or bi[BI.BitCount] != 24 or bi[
                BI.Compression] != 0:
                print("Unsupported file format.", file=sys.stderr)
                sys.exit(6)

            ouptr.write(outa)
            ouptr.write(outb)

            matrix = []  # 定义一个矩阵
            for i in range(0, abs(lst_bi[BI.Height])):  # 在0到height的范围
                du = []
                for j in range(0, bi[BI.Width]):  # 在0到width的范围
                    triple = inptr.read(3)
                    du.append(triple)
                matrix.append(du)
                inptr.seek(pad, 1)

            matrix2 = []
            for i in range(abs(lst_bi[BI.Height]) - 1, -1, -1):
                lst = []
                for j in range(bi[BI.Width]):
                    lst.append(matrix[i][j])
                # print(lst)
                matrix2.append(lst)

            matrix3 = []
            for j in range(bi[BI.Width]):
                tran = []
                for i in range(abs(lst_bi[BI.Height])):
                    tran.append(matrix2[i][j])
                matrix3.append(tran)

            for i in range(abs(lst_bi[BI.Height])):
                ling = b'0'
                hang = b''
                for j in range(0, bi[BI.Width]):
                    ouptr.write(matrix3[i][j])
                hang += ling * padding
                ouptr.write(hang)

            print("All folks")
            sys.exit(0)
