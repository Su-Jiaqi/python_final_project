# # -*- coding: UTF-8 -*-
# from PIL import Image
# import base64
# from io import BytesIO
#
#
# img=Image.open("what.bmp")
# print("图片的宽=%d"%img.width)
# print("图片的高=%d"%img.height)
#
# #图片的缩放
# resize_img=img.resize((50,50))
# resize_img.save("shrink.bmp")
#
# resize_img=img.resize((2000,2000))
# resize_img.save("enlarge.bmp")
#
# #图片的旋转
# img1=img.rotate(90)
# img1.save("旋转90°.bmp")
#
# img2=img.rotate(180)
# img2.save("旋转180°.bmp")
#
# img3=img.rotate(270)
# img3.save("旋转270°.bmp")


# -*- coding: UTF-8 -*-
import struct
import sys
import os


'''
uint8_t  BYTE   == B
uint32_t DWORD  == I
int32_t  LONG   == i
uint16_t WORD   == H
'''

if __name__ == '__main__':

    class BF():
        Type = 0
        Size = 1
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
        Blue=0
        Green=1
        Red=2



    if len(sys.argv) != 3:        #如果参数个数不为3。需要在cmd运行，在后边写明原bmp格式文件和新的bmp格式文件名称
        print("Usage: ./copy infile outfile")
        sys.exit(1)
                                  #这里的xxfile相当于xxptr的一个过度变量==打开文件的过度变量
    infile = sys.argv[1]          #原来的bmp格式图片被赋予变量名称infile
    outfile = sys.argv[2]         #新的bmp格式图片被赋予变量名称outfile
    inptr = open("what.bmp", "rb")    #“打开bmp原文件”被赋予变量名称inptr（相当于原来的bmp格式文件）
    outptr = open("k.bmp", "wb")  #“打开bmp新文件”被赋予变量名称outptr（相当于新的bmp格式文件）

    if inptr == None:
        print("Could not open", file=sys.stderr)
        sys.exit(2)

        inptr.close()
        print("Could not create", file=sys.stderr)
        sys.exit(3)

    ina=inptr.read(14)
    bf=struct.unpack('<HIHHI', ina)

    inb=inptr.read(40)
    bi=struct.unpack('<IiiHHIIiiII', inb)

    # bf=BITMAPFILEHEADER()
    # bi=BITMAPINFOHEADER()
    if bf[BF.Type]!= 0x4d42 or bf[BF.OffBits]!= 54 or bi[BI.Size]!= 40 or bi[BI.BitCount]!= 24 or bi[BI.Compression]!= 0:
    # if bf.bfType != 0x4d42 or bf.bfOffBits != 54 or bi.biSize != 40 or bi.biBitCount != 24 or bi.biCompression != 0:
        outptr.close()
        inptr.close()
        print( "Unsupported file format.",file=sys.stderr)
        sys.exit(4)

    outptr.write(ina)
    outptr.write(inb)

    padding = int((4 - (bi[1] * 3) % 4) % 4)  #一个像素占三个字节

    for i in range(0, abs(bi[BI.Height])):       #在0到height的范围
        for j in range(0, bi[BI.Width]):        #在0到width的范围
            triple=inptr.read(3)
            outptr.write(triple)
        for k in range(0, padding):
            pad=inptr.read(1)    #图像数据总大小 192 字节
            outptr.write(pad)
    inptr.close()
    outptr.close()
    print("All folks")
    sys.exit(0)























