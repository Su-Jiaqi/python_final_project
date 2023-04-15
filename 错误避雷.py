s=1.75
print(s) #>>1.75
print('I am s m tall') #>>I am s m tall
#字符串中的s是一个字符，和前边的变量s无关
#字符串必须用引号括起来，用引号括起来的就是字符串
print('I am \
(s)\
m tall')   #想输出“I am 1.75 m tall”
#>>I am (s)m tall
print('I am')
print(s)
print('m tall')  #>>I am （换行）1.75(换行)m tall
print('I am ',s,'m tall') #>> I am 1.75 m tall

a=4
b=5
print('a+b')#>>a+b   想要输出9？？？
print(a+b)  #>>9
#加引号是字符串  不加引号是变量
print('a+b=',a+b) #a+b=9

#字符串中的字符不能修改
#int把小数转成整数时,"四舍五入"而不是"四舍五入"
#input（）一次只输入一行，如果输入有多行，就用多次input（）

# %s表示此处要输出一个字符串
# %d表示此处要输出一个整数
# %f表示此处要输出一个小数
# %.nf表示此处要输出一个小数，保留小数点后面n位，四舍六入，五则可能入也可能舍。注意，有'.'
# 格式控制符只能出现在字符串中。