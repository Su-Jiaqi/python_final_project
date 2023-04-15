# -*- coding: UTF-8 -*-
import array
import sys
from struct import unpack

# if __name__ == '__main__':
#     # 以二进制形式打开文件
#     f = open('what.bmp', 'rb')
#     # 读取前44字节
#     info = f.read(54)
#     print(info)


# 读取并存储 bmp 文件
class ReadBMPFile:
    def __init__(self, filePath):
        file = open("what.bmp", "rb")
        # 读取 bmp 文件的文件头    14 字节
        self.bfType = unpack("<h", file.read(2))[0]  # 0x4d42 对应BM 表示这是Windows支持的位图格式
        self.bfSize = unpack("<i", file.read(4))[0]  # 位图文件大小
        self.bfReserved1 = unpack("<h", file.read(2))[0]  # 保留字段 必须设为 0
        self.bfReserved2 = unpack("<h", file.read(2))[0]  # 保留字段 必须设为 0
        self.bfOffBits = unpack("<i", file.read(4))[0]  # 偏移量 从文件头到位图数据需偏移多少字节（位图信息头、调色板长度等不是固定的，这时就需要这个参数了）
        # 读取 bmp 文件的位图信息头 40 字节
        self.biSize = unpack("<i", file.read(4))[0]  # 所需要的字节数
        self.biWidth = unpack("<i", file.read(4))[0]  # 图像的宽度 单位 像素
        self.biHeight = unpack("<i", file.read(4))[0]  # 图像的高度 单位 像素
        self.biPlanes = unpack("<h", file.read(2))[0]  # 说明颜色平面数 总设为 1
        self.biBitCount = unpack("<h", file.read(2))[0]  # 说明比特数

        self.biCompression = unpack("<i", file.read(4))[0]  # 图像压缩的数据类型
        self.biSizeImage = unpack("<i", file.read(4))[0]  # 图像大小
        self.biXPelsPerMeter = unpack("<i", file.read(4))[0]  # 水平分辨率
        self.biYPelsPerMeter = unpack("<i", file.read(4))[0]  # 垂直分辨率
        self.biClrUsed = unpack("<i", file.read(4))[0]  # 实际使用的彩色表中的颜色索引数
        self.biClrImportant = unpack("<i", file.read(4))[0]  # 对图像显示有重要影响的颜色索引的数目
        self.bmp_data = []

        if self.biBitCount != 24:
            print("输入的图片比特值为 ：" + str(self.biBitCount) + "\t 与程序不匹配")

        for height in range(self.biHeight):
            bmp_data_row = []
            # 四字节填充位检测
            count = 0
            for width in range(self.biWidth):
                bmp_data_row.append(
                    [unpack("<B", file.read(1))[0], unpack("<B", file.read(1))[0], unpack("<B", file.read(1))[0]])
                count = count + 3
            # bmp 四字节对齐原则
            while count % 4 != 0:
                file.read(1)
                count = count + 1
            self.bmp_data.append(bmp_data_row)
        self.bmp_data.reverse()
        file.close()
        # R, G, B 三个通道
        self.R = []
        self.G = []
        self.B = []

        for row in range(self.biHeight):
            R_row = []
            G_row = []
            B_row = []
            for col in range(self.biWidth):
                B_row.append(self.bmp_data[row][col][0])
                G_row.append(self.bmp_data[row][col][1])
                R_row.append(self.bmp_data[row][col][2])
            self.B.append(B_row)
            self.G.append(G_row)
            self.R.append(R_row)

    # h=int(input("需要图片的长："))
    # w=int(input("需要图片的宽："))
    #对图片进行处理
    def resize(self, width, height):
        self.__nni(width, height)

    # nearest_neighbor Interpolation
    def __nni(self, width, height):
        # width must be Multiple of four
        if width % 4 != 0:
            width -= width % 4
        w_ratio = (self.height / height)
        h_ratio = (self.width / width)
        # new pixels array
        new_bits = [b''] * height * width * self.bit_count
        for row in range(0, height):
            for col in range(0, width):
                for channel in range(0, self.bit_count):
                    old_r = round((row + 0.5) * w_ratio - 0.5)   # 这里的 +0.5 -0.5 就是对坐标进行转换
                    old_c = round((col + 0.5) * h_ratio - 0.5)
                    new_index = row * width * self.bit_count + col * self.bit_count + channel
                    old_index = old_r * self.width_step + old_c * self.bit_count + channel
                    new_bits[new_index] = self.bits[old_index]
        self.bits = new_bits
        # reset header info
        self.bfSize = i_to_bytes(height * width * self.bit_count + 54, 4)
        self.biSizeImage = i_to_bytes(len(new_bits), 4)
        self.biWidth = i_to_bytes(width, 4)
        self.biHeight = i_to_bytes(height, 4)

#另存图片
    # 修改文件指针移动到文件末尾
    f.seek(0, 2)
    # 报告文件指针，也就是文件大小
    print(f.tell())
    # 数组的长度为文件字节长度减去54个字节,除2为采样宽度
    n = (f.tell() - 54) // 2

    # 创建数组，储存data部分数据
    buf = array.array('h', [])

    # 将文件的数据读入到buf当中,不返回字符串
    f.seek(54)
    buf.fromfile(f, n)
    print(buf[0])
    print(len(buf))

    # 将数据存入到一个新文件
    f2 = open('hello.bmp', 'wb')
    f2.write(info)
    buf.tofile(f2)
    f2.close()



