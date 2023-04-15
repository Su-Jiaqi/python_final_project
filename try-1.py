#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

import sys      #调用sys库
import os       #调用os库
for i in sys.argv:   #对于列表中的所有的脚本命令行参数
	print(i)
os.system('pause')   #暂停命令，正在运行的文件会在命令行中暂停

if __name__ == '__main__':
    # 以二进制形式打开文件
    f = open('what.bmp', 'rb')
    # 读取前54字节
    info = f.read(54)
    print(info)

def wh(argc):
#ensure proper usage
    if argc != 3:                #是否收到了三个参数
        print("Usage: ./copy infile outfile\n")
        sys.exit(1)                 #主程序将以返回码 1 返回表示错误。

#remember filenames
    infile = argv[1];          #输入文件并定义为infile，作为第一个参数,程序自身运行目录路径和程序名
    outfile = argv[2];         #输入文件并定义为outfile，作为第二个参数,程序在DOS命令中执行程序名后的第一个字符串

#open input file
    inptr = open(infile, "r");       #r代表“只读”
    if inptr == NULL:                 #遇到输入位图无法打开或不存在的问题
        print("Could not open %s.\n", infile)      #输出“无法打开该文件”
        sys.exit(2)                      #主程序将以返回码 2 返回表示错误。

   ##open output file
    outptr = open(outfile, "w");     #w代表“只写”
    if outptr == NULL:               #遇到输出路径无法创建、不合法的问题
        inptr.close()                #关闭文件
    # close(inptr);
        print(stderr, "Could not create %s.\n", outfile)
        sys.exit(3)                    #主程序将以返回码 3 返回表示错误。


   #read infile's BITMAPFILEHEADER
    def BITMAPFILEHEADER(bf):                                 #定义文件头变量
        fread(bf, sizeof(BITMAPFILEHEADER), 1, inptr)        #读取文件头

    # read infile's BITMAPINFOHEADER
    def BITMAPINFOHEADER(bi):                                 #定义信息头变量
        fread(bi, sizeof(BITMAPINFOHEADER), 1, inptr)        #读取信息头

   # ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if bf.bfType != 0x4d42 and bf.bfOffBits != 54 and  bi.biSize != 40 and bi.biBitCount != 24 and bi.biCompression != 0:
    # 如果文件格式不是bm，文件头不是54位，位图信息头不是40
    #如果比比特计数不是24，双压缩不是0
    #遇到第三个参数不合法的问题（既不能解释为一个目标分辨率也不能解释为一个旋转角度）
        outptr.close()                                    #关闭文件流
        inptr.close()
        print(stderr, "Unsupported file format.\n")       #输出“文件参数不符合要求”
        sys.exit(4)                                         #主程序将以返回码 4 返回表示错误。


# 1.BMP图像的读:
# (1)首先定义BMP文件头和信息头变量BITMAPFILEHEADER bf; BMP文件头结构体BITMAPINFOHEADER bi; BMP信息头结构体
#
# (2)创建文件输入流 fp
# fp=fopen(fileName,“rb”); //fileName为BMP图像文件名
#
# (3)读取信息头、文件头fread(&bf,sizeof(BITMAPFILEHEADER),1,fp); fread(&bi,sizeof(BITMAPINFOHEADER),1,fp);
#
# 注：经过这两条程序把BMP图像的信息头、文件头赋给bf和bi变量，可以根据bf和bi得到图像的各种属性。



#C语言中char：char是c语言中最基本的数据类型之一，叫字符型，在内存中占用一个字节的空间，可以用于存放单个字符，也可以用于存放整数，
# char可以分为有符号和无符号两种类型
#Python中无char类型，单个字符也是字符串

# argv为argument vector的缩写，可以理解成参数序列
# argc为argument count的缩写，代表参数的个数

# fread是一个函数。从一个文件流中读数据，最多读取count个元素，每个元素size字节，
# 如果调用成功返回实际读取到的元素个数，如果不成功或读到文件末尾返回 0。
# fread 函数原型 :
# size_t fread( void *buffer, size_t size, size_t count, FILE *stream );
# void *buffer 参数 : 将文件中的二进制数据读取到该缓冲区中 ;
# size_t size 参数 : 读取的 基本单元 字节大小 , 单位是字节 , 一般是 buffer 缓冲的单位大小 ;
#       如果 buffer 缓冲区是 char 数组 , 则该参数的值是 sizeof(char) ;
#       如果 buffer 缓冲区是 int 数组 , 则该参数的值是 sizeof(int) ;
# size_t count 参数 : 读取的 基本单元 个数 ;
# FILE *stream 参数 : 文件指针 ;
# size_t 返回值 : 实际从文件中读取的 基本单元 个数 ; 读取的字节数是 基本单元数 * 基本单元字节大小 ;


















