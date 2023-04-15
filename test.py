# print("hello world")
# print("I love the world ")
# a=12
# b=a #让b的值变得和a一样
# print(a+b)
# a="hello"
# print(a)
#
# a="he"
# print(a) #>>he
# b=3+2
# a=b  #a的值变得和b一样
# print(b) #>>5
# print(a) #>>5
# b=b+a  #b的值改变为原来a+b的值
# print(b) #>>10
#
# a,b="he",12
# print(a,b) #>>he 12
# a,b=b,a #交换a，b的值
# print(a,b) #>>12,he
# c,a,b=a,b,a
# print(a,b,c) #he 12 12
# a=b=c=10
# print(a,b,c) #10 10 10
#
# x="I said:'hello'"
# print(x)  #>>I said :'hello'
# print('I said:"hello"') #>>I said:"hello"
# print('''I said:'he said "hello"'.''')#>>I said:'he said "hello"'
# print("this \
# is \
# good") #this is good 字符串太长时，可以分行写
# # print(hello,world) #错了！没有用引号括起来
#
# s=1.75
# print(s) #>>1.75
# print('I am s m tall') #>>I am s m tall
# #字符串中的s是一个字符，和前边的变量s无关
# #字符串必须用引号括起来，用引号括起来的就是字符串
# print('I am \
# (s)\
# m tall')   #想输出“I am 1.75 m tall”
# #>>I am (s)m tall
# print('I am')
# print(s)
# print('m tall')  #>>I am （换行）1.75(换行)m tall
# print('I am ',s,'m tall') #>> I am 1.75 m tall
#
# a=4
# b=5
# print('a+b')#>>a+b   想要输出9？？？
# print(a+b)  #>>9
# print('a+b=',a+b) #a+b=9
# print("苏佳琪学会了",'a+b=',a+b)
#
# print ('\t')
# print('what \n are ')
# para_str="""多行字符串可以使用制表符TAB(\t)
# 也可以使用换行符[\n]
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# """
# print(para_str)
#
# a='ABCD'
# print(a[-1])  #D
# print(a[0])  #A
# print(a[2])  #C
#
# a='ABCD'
# b='1234'
# a=a+b
# print(a)  #ABCD1234
# a=a+a[1]
# print(a)  #ABCD1234B
#
# a='Hello'
# b='Python'
# print('el' in a)   #True
# print('th' not in b)  #False
# print('lot' not in a)  #True
#
# a=15
# b='23'
# #c=a+b 错误 字符串和整数无法相加
# print(a+int(b))  #>>38
# print(str(a)+b)  #>>1523
# c=1+float ('3.5')
# print(c)          #>>4.5
# print(3+eval('4.5'))  #>>7.5
# print(eval("3+2"))    #>>5
# print(eval("3+a"))    #>>18
#
# print(int(3.2))  #>>3
# print(int(3.9))  #>>3
#
# print(1,2,3,end="")
# print(" ok")    #>>1 2 3 ok
#
# s=input("请输入你的名字：")
# print(s +",你好！")
#
# a=int(input())
# b=int(input())
# print(a+b)
# #会是空的 输入一个数字 回车 再一个数字 回车 输出加和
# #input（）一次只输入一行，如果输入有多行，就用多次input（）
#
# empty=[]
# list1=['Goole','Runoob',1997,2000]
# list2=[1,2,3,4,5,6,7]
# print("list1[0]",list1[0])
# list1[2]=2001   #更改了列表中下标为2 的元素
# a=2
# print("更新后的第三个元素为：",list1[a])  #变量也能做下标
# #>>更新后的第三个元素为：2001
#
# lst=[1,2,3,"4",5]
# print(4 in lst,3 in lst,"4" in lst) #>>False True True
#
# s=input()
# numbers=s.split()  #分割字符串
# print(int(numbers[0])+int(numbers[1]))
# #>>最开始为空格 输入两个数字 中间用空格隔开 输出为加和

# print("34\t\t45\n7".split())  #>>['34', '45', '7']
# #\t是制表符，\n是换行符号
# print("ab cd hello ".split())  #>>['ab', 'cd', 'hello']
# s="12 34"
# lst=s.split()
# print(lst)    #>>['12', '34']

# print(input().split()[2][1])  #>>2

# a=input()
# print("  "+a)
# print(" "+a+a+a)
# print(a*5)
# #>>  5
#     555
#    55555

# s=input().split()      #输入2 3 5 >>25
# a,b,c=int(s[0]),int(s[1]),int(s[2])
# print((a+b)*c)

# n=input()               #输入abc
# print(n[2]+n[1]+n[0])   #>>cba

# a=int(input("请输入第一个整数:"))
# b=int(input("请输入第二个整数:"))
# c=a+b
# print("a+b=",c)

# print(3<5)   #>>True
# print(4!=7)  #>>True
# a=4
# print(2<a<6<8)  #>>True
# print(2<a==4<6) #>>True
# print(2<a>5)    #>>False
# b=a<6
# print(b)        #>>True
# print(b==1)     #>>True
# print(b==2)     #>>False
# b=a>6
# print(b==0)     #>>True
# a=True
# print(a==1)     #>>True

# a="k"
# print(a=="k")      #>>True
# a="abc"
# print(a=="abc")    #>>True
# print(a=="Abc")    #>>False
# print("abc<acd")   #>>abc<acd
# print("abc<abcd")  #>>abc<abcd
# print("abc">"Abc") #>>True

# a=float(input("请输入第一个边长："))
# b=float(input("请输入第二个边长："))
# c=float(input("请输入第三个边长："))
# p=0.5*(a+b+c)
# s=(p*(p-a)*(p-b)*(p-c))**0.5
# print(s)

# if int(input())==5:
#     print("a",end="")
#     print("b")

# if "ok":
#     print("ok")  #>>ok
# if "":
#     print("null string")  #>>无输出
# a=[4,2]
# if a:
#     print(a)  #>>[4,2]
# if 20:
#     print(20)    #>>20
# if 0:
#     print(0)

# m=int(input("请输入正整数m："))
# n=int(input("请输入正整数n："))
# if m>n:
#     p=m
#     m=n
#     n=p
# print((n+m)*(n-m+1)*0.5)

# a=int(input())
# if a>0:
#     if a%2:
#         #>>如果a整除2，则余数是0，是“假的”；不是0，是“真的”，输出good
#         #>>%代表取余数
#         print("good")
#     else:
#         print("bad")

# password="python"
# userInput=input()
# if userInput==password:
#     print("对了！")
# else:
#     print("错了！")

# #摄氏温度和华氏温度的转换
# tmpStr=input("请输入带有符号的温度值：“")   #tmpStr是变量名称，任意取
# if tmpStr[-1]in['F','f']:#如果输入华氏温度
#     C=((float(tmpStr[0:-1])))-32/1.8
#     print("转换后的温度是"+str(C)+"C")
# elif tmpStr[-1] in     "Cc"  :  #如果输入摄氏温度
#     F=1.8*eval(tmpStr[0:-1])+32
#     print("转换后的温度是"+str(F)+"F")  #str将F转字符串
# else:
#     print("输入格式错误")
#用float代替eval也可以

# 字符串切片
# 若s是一个字符串
# 则:
# s[x:y]是s的从下标x到下标y的左边那个字符构成的子串(切片)
# print("12345"[1:3])  #>>23
# a="abcdef"
# print(a[2:-1])  #>>cde
# print(a[0:6])   #>>abcdef

#判断年份
# year=int(input("请输入年份："))
# if year <=0:
#     print("Illegal year")
# else:
#     print("Leaglal year")
#     if year>1949 and (year-1949)%10==0:#建国整十年
#         print("Lucky year")
#     elif year>1921 and not((year-1921)%10):  #建党整十年
#         #只是为了掩饰not的用法，没必要这么写
#         print("Good year")
#     elif year %4==0and year%100 or year %400==0:
#         #year%100若不为0，则year%100就相当于True
#         print("Leap year")  #闰年
#     else:
#         print("Common year.")


# a=int(input("请输入一个整数："))
# b=radom(  )
#
# h=1.746
# print("My name is %s,I am %.2fm tall."% ("tom",h))   #>>My name is tom,I am 1.75m tall.
# print("My age is %d."%18)     #>>My age is 18.
# print("%d%s"%(18,"hello"))    #>>18hello
# print("%.2f,%.2f"%(5.225,5.325))   #>>5.22,5.33

#输入，只有一行，共有三个参数，其中第1，2个参数为整数，第三个参数为操作符（+-*/）
#如果出现除数为零的情况，则输出：Divided by zero！
#如果出现无效操作复，则输出：Invalid operator！
# s=input().split()
# a,b,c=int(s[0]),int(s[1]),s[2]
# if c in ["+","-","*","/"]:
#     if c=="+":
#         print(a+b)
#     elif c=="-":
#         print(a-b)
#     elif c=="*":
#         print(a*b)
#     else:
#        if b==0:
#            print("Divided by zero!")
#        else:
#            print(a//b)
# else:
#     print("Invalid operator！")

# s=int(input())
# if s<0:
#     s=-s
# def isprime(s):
#     if s <= 1:
#         return 0
#     if s==2:
#         return 1
#     for :
#         if s%i==0:
#             return 0
#     return 1
# for i in range (2,n):
#     if isprime(i)==1:
#         print(i,end=",")

# s=int(input())
# for i in range (1,s):
#     if s%i==0:
#         print("不是素数")
#     else:
#         print("是素数")
#
# s=int(input())
# for i in range ():
#     if s%i==0:

# a=int(input())
# if a<0:
#     a=-a
# if a==0:
#     b="不是素数"
# elif a==1:
#     b="不是素数"
# else:
#     lst=[]
#     for i in range (1,a+1):
#         c=a%i
#         if c==0:
#             lst.append(i)
#     lst_len=len(lst)
#     if lst_len==2:
#         b="是素数"
#     else:
#         b="不是素数"
# print(b)

# a=int(input())
# if a<0:
#     a=-a
# if a==0:
#     b=0
# else:
#     lst=[]
#     for i in range(1,a+1):
#         c=a%i
#         if c==0:
#             lst.append(i)
#     b=len(lst)
# print(b)

# p=int(input("请输入第一个正整数："))
# q=int(input("请输入第二个正整数："))
# if p<q:
#     m=p
#     p=q
#     q=m
# R=p%q
#
# while R!=0:
#     p=q
#     q=R
#     R=p%q
# print(R)




# if R!=0:
#     p=q
#     q=R
#     R=p%q
# while R==0:
#     print(q)

# for i in range (5):   #[0,5)
#     print(i)          #>>0/1/2/3/4/
# for i in range (5,9): #[5,9)
#     print(i)          #>>5/6/7/8

# for i in range (0,10,3):   #步长是3
#     print(i)               #0、3、6、9
# for i in range (0):

# a=['Goole','Baidu','IBM','Taobao','QQ']
# for i in range (len(a)):  #len,求列表长度（元素个数）
#     print(i,a[i])
#>>0 Goole
# 1 Baidu
# 2 IBM
# 3 Taobao
# 4 QQ

# for letter in 'Taobao':
#     print(letter)    #>>分行打出每一个字母
#
# sites=["Baidu","Google","IBM","Taobao"]
# for site in sites:
#     if site =="IBM":
#         print("OK")
#     print("site:"+site)
# else:
#     print("No break")
# print("Done!")
# >>
# OK
# site:IBM
# site:Taobao
# No break
# Done!

# sites=["Baidu","Google","IBM","Taobao"]
# for site in sites:  #对sites中的每一个值 site
#     if site=="IBM":
#         print("OK")
#         break
#     print("site:"+site)
# else:
#     print("No break")
# print("Done!")
# >>
# site:Baidu
# site:Google
# OK
# Done!

# for letter in "Taobao":
#     if letter =='o':   #字母为o时跳过输出
#         continue       #直接跳到下次循环
#     print('当前字母：',letter )
# >>
# 当前字母： T
# 当前字母： a
# 当前字母： b
# 当前字母： a

# for i in range (26):
#     print(chr(ord("a")+i),end="")
#>>abcdefghijklmnopqrstuvwxyz
# ord(x) 求字符x编码（字符就是长度为1的字符串）
# chr(x) 求编码为x的字符

# for i in range (10):
#     print(chr(ord("0")+i),end="")
# #>>0123456789


# n=int(input())
# sum=1
# for i in range(1,n):
#     sum*=int(input())
# print(sum)

# n=int(input())
# total=0
# for i in range (n):     #做n次
#     total=total+int(input())   #每次读入一行
# print(total)
# #第一次输入的数是循环次数，后面输入的是求和的数字

# 从小到大输出n的因子
# n=int(input())
# for x in range (1,n+1):
#     if n%x==0:
#         print(x,"",end="")

# 从大到小输出n的因子
# n=int(input())
# for x in range (n,0,-1):
#     if n % x == 0:
#          print(x,"",end="")

# 多重循环
# 多次求n个数的和
# m=int(input())
# for i in range (m):   #m组数据，所以要处理n次
#     n=int(input())
#     total=0
#     for i in range (n):#n个数，每个一行，所以要input  n次
#         total+=int(input())
#     print(total)

# # 给定正整数n和m，在1至n这n个数中，取出两个不同的数，使得其和是m的因子，问有多少种不同的取法。输出这些取法。
# total=0 #取法总数
# lst=input().split()
# n,m=int(lst[0]),int(lst[1])
# for i in range (1,n):
#     for j in range (i+1,n+1):
#         if m % (i+j)==0:
#             print(i,j)
#             total+=1
# print(total)

# # 多重循环中的break
# # 只会跳出当前那重循环，不会跳出多重循环
# # 给定正整数n和m，在1至n这n个数中，取出两个不同的数下，一，使得x<y且x+y是m的因子。要求输出的数对里边，x不重复，且y尽可能小。输出这些取法。
# lst=input().split()
# n,m=int(lst[0]),int(lst[1])
# for i in range (1,n):  #取第一个数i，共n-1种取法
#     for j in range (i+1,n+1):   #取第二个数比第一个数大，以免取法重复
#         if m %(i+j)==0:
#             print(i,j)
#             break    #后面的j不用再取了，直接换下一个

#while 循环
# count=0
# while count<5:
#     print(count,"小于5")
#     count=count+1
# else:
#     print(count,"大于或等于5")
# #>>
# # 0 小于5
# # 1 小于5
# # 2 小于5
# # 3 小于5
# # 4 小于5
# # 5 大于或等于5

# 连续输出26个字母
# i=0
# while i<26:
#     print(chr(ord("a")+i),end="")
#     i+=1
#>>abcdefghijklmnopqrstuvwxyz

# #输入一个正整数n，从小到大输出它所有的因子
# n=int(input())
# x=1
# while x<=n:
#     if n%x==0:
#         print(x,"",end="")
#     x+=1

# while(input("请输入密码：")!="pku"):
#     print("密码不正确！")
# print("密码输入成功！")

# 输入三个整数，求他们的最小公倍数
# s=input().split()
# x,y,z=int(s[0]),int(s[1]),int(s[2])
# n=1
# while True:
#     if n%x==0and n%y==0 and n%z==0:
#         print(n)
#         break
#     n=n+1

#或者：
# s=input().split()
# x,y,z=int(s[0]),int(s[1]),int(s[2])
# n=1
# while not (n%x==0 and n%y==0 and n%z==0):
#     n+=1
# print(n)

# 改进：即便是枚举，没必要试的，也不要去试，这样速度才快
# s=input().split()
# x,y,z=int(s[0]),int(s[1]),int(s[2])
# n=m=max(x,y,z)
# while True:
#     if n%x==0 and n%y==0 and n%z==0:
#         print (n)
#         break
#     n+=m   #没必要哦一个一个试，而是每隔m个试一下（还可以进一步改进）
#
#
# # 输入若干行，每行若干整数，求所有整数的最大值
# s=input()
# lst=s.split()
# maxV=int(lst[0])
# try:
#     while True:
#         lst=s.split()
#         for x in lst:
#             maxV =max(maxV,int(x))
#         s=input()   #输入数据已经没有了还执行input，会产生异常
# except:
#     pass
# print(maxV)
# #quit退出输入或者按Ctrl+D   Ctrl+z在cmd下执行

#1.n!
# a=int(input())
# b=a
# for i in range (a-1,0,-1):
#     b*=i
# print(b)

#2.计算π的近似值
# eps=int(input())
# pai_4=0
# sign=1
# denominator=0
# for j in range(0,eps):
#     denominator=2*(j+1)-1
#     pai_4+=sign*(1/denominator)
#     sign=-sign
# pai=4*pai_4
# print(pai)

#3.计算Fibonacci序列的第n项(数列找规律)
# F0,F1=0,1
# n=int(input())
# if n==0:
#     output=0
# elif n==1:
#     output=1
# else:
#     lst=[0]*(n+1)
#     lst[1]=1
#     for k in range(2,n+1):
#         lst[k]=lst[k-1]+lst[k-2]
#     output=lst[n]
# print(output)

#4.输入N个整数放在一个列表中，然后从后向前显示列表中的所有元素。
# c=list(map(int,input().split()))
# c_new=c[ : :-1]
# print(c_new)

#5.编写函数，计算列表中整数元素的最大值、最小值和平均值。
# d=list(map(int,input().split()))    #map函数 把列表里的字符串转化为int
# maxinum=max(d)
# mininum=min(d)
# averagenum=sum(d)/len(d)
# print(maxinum)
# print(mininum)
# print(averagenum)

# try:
#     n=int(input())
#     print("hello")
#     a=100/n
#     print(a)
# except:
#     print("error")
# print("end")

#求斐波那切数列第k项
# k=int(input())
# if k==1 or k==2:
#     print(1)
# else:
#     a1=a2=1
#     for i in range (k-2):
#         a1,a2=a2,a1+a2
#     print(a2)

# 输入三角形的三条边， 计算该三角形的面积。计算前应判断输入的三个值能否构成三角形。
# a=int(input())
# b=int(input())
# c=int(input())
# p=0.5*(a+b+c)
# if a+b>c and a+c>b and b+c>a:
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# else:
#     print("不能构成三角形")

#回文数是逆序后与原数相等的数,例如1221,逆序还是1221,是回文数;而1234逆序为4321,不是回文数。
# 输入一个4位的整数,判断该数是否为回文数。注意,本题用整数实现。
# n=int(input("请输入一个四位整数："))
# a=n//1000
# b=(n-1000*a)//100
# c=(n-1000*a-100*b)//10
# d=n-1000*a-100*b-10*c
# m=1000*d+100*c+10*b+a
# if m==n:
#     print("是回文数")
# else:
#     print("不是回文数")

#输入一个小于等于1000 的整数表示总金额， 等价的表示成各种面额纸币的张数， 使得纸币张数最少。
# 设可以提供的纸币面额分别是100 、50 、20 、10 、5 、1 元。
# n=int(input())
# if n>1000:
#     print("error")
# else:
#     a = n // 100
#     b = (n - 100 * a) // 50
#     c = (n - 100 * a - 50 * b) // 20
#     d = (n - 100 * a - 50 * b - 20 * c) // 10
#     e = (n - 100 * a - 50 * b - 20 * c - 10 * d) // 5
#     f = n - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e
#     print("100元", a, "张")
#     print("50元", b, "张")
#     print("20元", c, "张")
#     print("10元", d, "张")
#     print("5元", e, "张")
#     print("1元", f, "张")
# a=n//100
# b=(n-100*a)//50
# c=(n-100*a-50*b)//20
# d=(n-100*a-50*b-20*c)//10
# e=(n-100*a-50*b-20*c-10*d)//5
# f=n-100*a-50*b-20*c-10*d-5*e
# print("100元",a,"张")
# print("50元",b,"张")
# print("20元",c,"张")
# print("10元",d,"张")
# print("5元",e,"张")
# print("1元",f,"张")

#1.输入三角形三个顶点的坐标，计算该三角形的面积。要求将计算两点之间距离单独编写成一个函数。
# x1=int(input("请输入x1："))
# x2=int(input("请输入x2："))
# x3=int(input("请输入x3："))
# y1=int(input("请输入y1："))
# y2=int(input("请输入y2："))
# y3=int(input("请输入y3："))
# s1=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
# s2=(((x3-x2)**2)+((y3-y2)**2))**(1/2)
# s3=(((x3-x1)**2)+((y3-y1)**2))**(1/2)
# s=(s1+s2+s3)/2
# area=(s*(s-s1)*(s-s2)*(s-s3))**(1/2)
# print("面积：%f"%(area))

# a=int(input("请输入一个数字："))
# b=int(input("请输入一个数字，决定相加个数"))
# sum=0
# c=a
# print("sum=",end="")
# for i in range(1,b+1):
#     if i!=b:
#         print("%d+"%a,end="")
#     else:
#         print("%d"%a,end="=")
#     sum=a+sum
#     a=a+c*(10**i)
# print(sum)

#3. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...，求出这个数列的前 20 项之和。注意，这个序列的特点是后一项的分子是前一项分子分母的和，后一项的分母是前一项的分子。
# a = 2.0
# b = 1.0
# s = 0.0
# for n in range(1,21):
#     s=s+a/b
#     b,a = a , a + b
# print(s)

#4. 编写函数，求两个数的最大公因数。编写主程序，输入两个整数，调用函数求最大公因数，在主程序中输出最大公因数。
# a=int(input())
# b=int(input())
# if b>a:    #让a一定不小于b
#     m=b
#     b=a
#     a=m
# list=[]
# for i in range (b,0,-1):
#     if a%i==0 and b%i==0:
#         list.append(i)
# factor_max=max(list)
# print(factor_max)

# #5.一个数如果恰好等于它的所有因子（不包括它本身）之和，这样的数称为完全数。
# lst=[]
# for i in range (1,1001):
#     a=0
#     for j in range (1,i):
#         if i%j==0:
#             a+=j
#     if i ==a:
#         lst.append(i)
# print(''. join (str(k) for k in lst))

# #2.编写函数，将十进制整数转换为二进制形式（用字符串表示），返回二进制形式的字符串，在主程序中输入十进制整数，
# # 调用函数转换为二进制（字符串形式），显示二进制数。
# # 例如，输入：12，输出：1100，要求不能使用Python中的转换函数直接转换，要自己通过除以2取余的运算进行转换。

# if n==0:
#     print(n)
# elif n>0 and n<2:
#     print(n)
# n=int(input())
# lst1=''
# while n>=0:
#     a=n%2
#     lst1.append(a)
#     n=(n-a)/2
# out_lst=list(map(int,lst1))
# print(str(out_lst))


# a=eval(input('请您输入十进制数：'))
# m=''
# while a>0:
#     m+=str(a%2)  #a对2求余，添加到字符串m最后
#     a=a//2
# print(m[::-1])   #反向输出
# 用函数实现十进制与二进制的转换

# test_list=['1','3','2','6','8']
# print("Original list is: " + str(test_list))
# out_list=list(map(int,test_list))
# print("Out list is: " + str(out_list))




# elif n>=2:
#     lst1 = []
#     a=n%2
#     lst1.append(a)
# n=(n-a)/2
#
#
# if n<0:
#     n=-n
#     if n > 0 and n < 2:
#         print(n)
#     elif n >= 2:
#         lst1 = []
#         a = n%2
#         lst1.append(a)
#         n = (n - a) / 2

# #2.编写函数，将十进制整数转换为二进制形式（用字符串表示），返回二进制形式的字符串，在主程序中输入十进制整数，
# # 调用函数转换为二进制（字符串形式），显示二进制数。
# # 例如，输入：12，输出：1100，要求不能使用Python中的转换函数直接转换，要自己通过除以2取余的运算进行转换。
# n=int(input())
# # #先处理正数情况
# if n==0:
#     print(str(n))
# elif n==1:
#     print(str(n))
# elif n>1:
#     lst=[]
#     while n>1:
#         a=n%2
#         lst.append(a)
#         n=n//2
#     lst.append(n)
#     lst=lst[::-1]
#     lst=''.join(map(str,lst))
#     print(lst)
# #处理负数情况
# else:
#     n=-n
#     lst=[]
#     while n>1:
#         a=n%2
#         lst.append(a)
#         n=n//2
#     lst.append(n)
#     # lst=lst[::-1]
#     b=len(lst)
#     c=b%8
#     d=8-c   #要添加d个0
#     e=1
#     while e<=d:
#         lst.append(0)
#         e+=1
#     lst = lst[::-1]
#     # lst=''.join(map(str,lst))
#     # lst=[str(x) for x in lst]
#     lst2=[2 if i==0  else i  for i in lst]
#     lst3=[0 if i==1 else i  for i in lst2]
#     lst=[1 if i==2 else i  for i in lst3]
#
#     for i in range(len(lst) - 1, -1, -1):
#         if i == len(lst) - 1:
#             lst[i] += 1
#         if lst[i] == 2:  # 如果出现2就变0,下一位进位
#             lst[i] = 0
#             if i > 0:
#                 lst[i - 1] += 1
#             else:  # 如果最后一位也需要进位则需添加一项
#                 n = int(1)
#                 lst.insert(0, n)  # insert函数,向列表头部添加元素
#
#     lst = ''.join(map(str, lst))
#     print(lst)

#幻方判断
#思路；
#1，先确定输入m，n，即要输入n个分别有m个元素的列表，并将所有的数组成一个矩阵
#2.判断矩阵是否是方阵 是 则继续，否 则终止 输出error
#3.计算每一行，每一列，对角线 上所有数字的加和，判断是否想等。是，输出true；否，输出false。

# lst1 = []
# while len(lst1)<m:
#     input(m)
#     lst1.append(m)

# def arr_size(arr, n):
#     size=int(len(a) / n)
#     s = []
#     for i in range(0, int(len(arr)) + 1, size):
#         c = arr[i:i + size]
#         if c != []:
#             s.append(c)
#     return s
#
# a=list(input("请输入所有数：").split())
# n=int(input("请输入矩阵行数："))
# # n = 4  # 等分成n份
# if __name__ == '__main__':
#     # a = [1, 2, 3, 4, 5, 6, 7, 8]
#     print(arr_size(a, n))
#
# # a=list(input("请输入所有数：").split())
# k=n//m
# if m!=k:
#     print("error!")
# else:

# 3. 编写函数，将十进制小数转换为二进制小数，返回二进制小数的字符串形式，最多保留到小数点后4位。编写主程序，输入小数，调用函数转换为二进制显示。
# m=float(input())
# n=int(m)
# # print(n)
# #先处理正数情况
# if n==0:
#     print(str(n))
# elif n==1:
#     print(str(n))
# elif n>1:
#     lst=[]
#     while n>1:
#         a=n%2
#         lst.append(a)
#         n=n//2
#     lst.append(n)
#     lst=lst[::-1]
#     lst=''.join(map(str,lst))
#     # print(lst)
# #处理负数情况
# else:
#     n=-n
#     lst=[]
#     while n>1:
#         a=n%2
#         lst.append(a)
#         n=n//2
#     lst.append(n)
#     # lst=lst[::-1]
#     b=len(lst)
#     c=b%8
#     d=8-c   #要添加d个0
#     e=1
#     while e<=d:
#         lst.append(0)
#         e+=1
#     lst = lst[::-1]
#
#     lst2=[2 if i==0  else i  for i in lst]
#     lst3=[0 if i==1 else i  for i in lst2]
#     lst=[1 if i==2 else i  for i in lst3]
#
#     for i in range(len(lst) - 1, -1, -1):
#         if i == len(lst) - 1:
#             lst[i] += 1
#         if lst[i] == 2:  # 如果出现2就变0,下一位进位
#             lst[i] = 0
#             if i > 0:
#                 lst[i - 1] += 1
#             else:  # 如果最后一位也需要进位则需添加一项
#                 n = int(1)
#                 lst.insert(0, n)  # insert函数,向列表头部添加元素
# # print(lst)
# #     lst = ''.join(map(str, lst)) #把列表转化为字符串
# #
# #处理小数部分：
# a=int(m)      #转化为2进制的时候，n已经发生了改变，不再是m的整数部分，所以要重新定义a
# k=m-a         #k定义为m的小数部分
# # print(k)
# # print(a)
# b=1
# while b<=4:
#     d=k*2
#     lst4=[]
#     if d>=1:
#         lst4.append(1)
#     else:
#         lst4.append(0)
#     b+=1
# lst6=[]
# lst6.append(lst)
# lst6.append(".")
# lst6.append(lst4)
# lst6=''.join(map(str, lst6)) #把列表转化为字符串
# print(lst6)

# n=float(input())
# m=int(n)
# k=m-n
# print(m)
# print(k)

# import math
# n=input()
# a,b=math.modf(n)
# print(a)
# print(b)

# #10进制转2进制完整版
# # 定义函数,计算整数部分
# def integer_cal(n):
#     if n < 0:  # n为负数的情况
#         n = -n
#
#         lst = []
#         while n > 1:
#             a = n % 2
#             lst.append(a)
#             n = n // 2
#         lst.append(n)
#         lst_len = len(lst)
#         if lst_len % 8 != 0:  # 如果列表元素个数是8的倍数则不用加零;不是8的倍数则需要补0
#             num_add = 8 - lst_len % 8
#             for k in range(0, num_add):  # 添加除以8所得余数个0
#                 m = int(0)
#                 lst.append(m)
#
#         lst = lst[:: -1]  # 列表倒置
#         lst = ['one' if k == 1 else k for k in lst]  # 19-21行,将1变为0,0变为1
#         lst = [1 if k == 0 else k for k in lst]
#         lst = [0 if k == 'one' else k for k in lst]
#
#         # 25-34行,二进制+1过程
#         for i in range(len(lst) - 1, -1, -1):
#             if i == len(lst) - 1:
#                 lst[i] += 1
#             if lst[i] == 2:  # 如果出现2就变0,下一位进位
#                 lst[i] = 0
#                 if i > 0:
#                     lst[i - 1] += 1
#                 else:  # 如果最后一位也需要进位则需添加一项
#                     n = int(1)
#                     lst.insert(0, n)  # insert函数,向列表头部添加元素
#         return lst
#
#     elif n > 0:  # n为正数的情况
#         if n == 1:
#             return [1]
#         else:
#             lst_1 = []
#             while n > 1:
#                 a = n % 2
#                 lst_1.append(a)
#                 n = n // 2
#             lst_1.append(n)
#             lst_1 = lst_1[:: -1]
#             return lst_1
#
#     elif n == 0:  # n为0的情况
#         lst_2 = [0]
#         return lst_2
#
#
# # 定义函数,计算小数部分
# def decimal_cal(m):
#     b = 1
#     lst2 = []
#     while b <= 4:  # 循环精度为4
#         m = m * 2
#         if m >= 1:
#             lst2.append(1)
#             m = m - 1
#         else:
#             lst2.append(0)
#         b += 1
#     return lst2
#
#
# Input = float(input())  # 输入任意有理数
#
# # x为实数的整数部分,y为小数部分
# if Input > 0:
#     x = int(Input)
#     y = Input - x
# elif Input < 0:
#     x = int(Input)
#     y = x - Input
# else:
#     x = 0
#     y = 0
#
# lst_integer = integer_cal(x)  # 调用函数,计算整数部分
# lst_decimal = decimal_cal(y)  # 调用函数,计算小数部分
# lst_all = []
#
# # 合并整数和小数
# for i in lst_integer:
#     lst_all.append(i)
# lst_all.append('.')
# for j in lst_decimal:
#     lst_all.append(j)
# lst_all = ' '.join(map(str, lst_all))
# print(lst_all)

# 一个数如果倒过来还是这个数，则这样的数称为回文数。例如，12321 倒过来还是 12321，所以，12321 是回文数。1234，倒过来是 4321，它不是回文数。
# 输入一个整数，判断它是否为回文数。提示：借助整除和求余运算进行。
# s=input()
# m=len(s)
# n=int(s)
# x=m
# lst=[]
# while x>=1:
#     a=n//(10**(m-1))
#     lst.append(a)
#     n-=a*(10**(m-1))
#     m-=1
#     x-=1
# lst=lst[::-1]
# lst=''.join(map(str, lst))
# y=int(lst)
# s=int(s)
# if y==s:
#     print("是回文数")
# else:
#     print("不是回文数")

# # 1. 输入某年某月某日，判断这一天是这一年的第几天，程序中要对输入的年份、月份和日是否有效进行判断。
# a=int(input("请输入年份："))
# b=int(input("请输入月份："))
# c=int(input("请输入日："))
# if b==1:
#     print(c)
# elif b==2:
#     print(31+c)
# else:
#     if 0==a//4 and 0!=a//100:
#         if b==3:
#             print(c+60)
#         elif b==4:
#             print(c+91)
#         elif b==5:
#             print(c+121)
#         elif b==6:
#             print(c+152)
#         elif b==7:
#             print(c+182)
#         elif b==8:
#             print(c+213)
#         elif b==9:
#             print(c+244)
#         elif b==10:
#             print(c+274)
#         elif b==11:
#             print(c+305)
#         elif b==12:
#             print(c+335)
#     elif 0==a//400:
#         if b==3:
#             print(c+60)
#         elif b==4:
#             print(c+91)
#         elif b==5:
#             print(c+121)
#         elif b==6:
#             print(c+152)
#         elif b==7:
#             print(c+182)
#         elif b==8:
#             print(c+213)
#         elif b==9:
#             print(c+244)
#         elif b==10:
#             print(c+274)
#         elif b==11:
#             print(c+305)
#         elif b==12:
#             print(c+335)
#     else:
#         if b==3:
#             print(c+59)
#         elif b==4:
#             print(c+90)
#         elif b==5:
#             print(c+120)
#         elif b==6:
#             print(c+151)
#         elif b==7:
#             print(c+181)
#         elif b==8:
#             print(c+212)
#         elif b==9:
#             print(c+243)
#         elif b==10:
#             print(c+273)
#         elif b==11:
#             print(c+304)
#         elif b==12:
#             print(c+334)

# 2.输出100以内的孪生素数，判断素数部分单独编写为一个函数，孪生素数是指相差为2的素数，例如3和5，11和13等。
# lst=[]
# for n in range (1,100):
#     for i in range(2, n):
#        if n%i==0:
#           break
#        else:
#            lst.append(n)
# print(lst)

# lst=[]
# i=2
# for i in range (2,100):
#     j=2
#     for j in range (2,i):
#         if i%j==0:
#             break
#     else:
#             lst.append(i)
# print(lst)

# def isprime(n):
#     if n<=1:
#         return 0
#     if n==2:
#         return 1
#     for i in range (2,n):
#         if n%i==0:
#             return 0
#     return 1
# for i in range (1,100):
#         if isprime(i)==1 and isprime(i+2)==1:
#              print(i,i+2)

# b=len(lst)
# for i in range (0,b-1):
#     if lst[i+1]-lst[i]==2:
#         lsti=[]
#         lsti.append(lst[i],lst[i+1])
# print(lsti)

# # 3.输入某人的身高(m)和体重(kg)，计算此人的BMI（身高体重指数），
# # 计算方法是体重除以身高的平方，然后根据BMI判断体重类型，体重类型分为四个
# # 标准如下：体重指数<18.5 为体重偏瘦，在18.5~23.9之间为正常，在24~27.9之间为偏胖，>=28为肥胖
# a=int(input("请输入体重："))
# b=int(input("请输入身高："))
# c=a/(b*b)
# if c<=18.5:
#     print("偏瘦")
# elif 18.5<c<23.9:
#     print("正常")
# elif c>=23.9:
#     print("偏胖")

# 1. 将数字1~6分别填入连续的6个方格中，使得相邻的两个数字之和为素数，输出所有满足条件的组合。
# 例如，其中一种组合是：4 1 6 5 2 3
# a=int(1)
# b=int(2)
# c=int(3)
# d=int(4)
# e=int(5)
# f=int(6)
#
# for i in range (2,n):
#     if n%i==0:
#
# list=[]
# for i in range (1,7):
#     list.append()
#
# def  Pailie(list1,start,end):
#     if start==end:
#         print(list1)
#     else:
#         for i in range(start,end+1):
#             list1[start],list1[i]=list1[i],list1[start]
#             #将第i个元素与首位元素交换
#             Pailie(list1,start+1,end)
#             #子序列进行全排列
#             list1[start], list1[i] = list1[i], list1[start]
#             #将i个元素放回原位置，准备下一个元素的交换
# list1=[1,2,3,4,5,6]
# Pailie(list1,0,len(list1)-1)
# lst=[]
# for i in list1:
#     for k in range (1,i):
#         if (list1[i]+list1[i+1])%k==0:
#             lst.append()
# print(lst)
# for i in list1:
#     if k in range (1,i):
#         (2i+1)%k==0
# print(143256)
# print(165234)
# print(234165)
# print(256143)
# print(325614)
# print(341256)
# print(341652)
# print(416523)
# print(432165)
# print(523416)
# print(561234)
# print(561432)
# print(614325)
# print(634125)
# print(654123)
# print(654321)










# 3、编写函数，将十进制整数转换为N进制形式，N小于等于16，
# 结果用字符串表示，在主程序中输入十进制整数和要转换的进制，
# 调用该函数转换为N进制数，要求通过除以N取余的运算转换。
# 提示，程序中先定义：str0='0123456789ABCDEF'

# n=int(input("请输入一个十进制数："))
# m=int(input("要转换的进制："))
# if m>16:
#     print("error")
# else:
#     if n==0:
#         print(str(n))
#     elif n<=m:
#         print(str(n))
#     elif n>m:
#         list = []
#         while n>m:
#            a=n%m
#            list.append(a)
#            n=n//m
#            list.append(n)
#         list=list[::-1]
#         list = ''.join(map(str, list))
#     print(list)
#整数
# n=int(input("请输入一个十进制数："))
# m=int(input("要转换的进制："))
# def f(n,m):
#     str0 = '0123456789ABCDEF'
#     lst=[]
#     while n>0:
#         a=n%m
#         lst.append(str0[a])
#         n//=m
#     lst=lst[::-1]
#     lst=''.join(lst)
#     return lst
# print(f(n,m))
#小数
# n=float(input("请输入一个十进制小数："))
# m=int(input("要转换的进制："))
# # n=k-abs(k)
# def f(n,m):
#     str0 = '0123456789ABCDEF'
#     lst=[]
#     while len(lst)<4:
#         a=n*m
#         a=int(a)
#         lst.append(str0[a])
#         n=(n*m)%1
#     lst=lst[::-1]
#     lst=''.join(lst)
#     return '0.'+ lst
# print(f(n,m))

#斐波那契
# k=int(input())
# if k==1 or k==2:
#     print(1)
# else:
#     a1=a2=1
#     for i in range (k-2):   #默认从0开始，步长是1
#         a1,a2=a2,a2+a1
#         print(a2)

#求阶乘
#方法一： 运用while循环
# k=int(input())
# if k==1:
#     print(1)
# else:
#     a=k
#     n=1
#     while a>1:
#         n=n*a
#         a=a-1
#     print(n)

#求阶乘的和
#方法二：运用range
# n=int(input())
# s=0
# for i in range (1,n+1):
#     f=1  #存放i阶乘
#     for j in range (1,i+1):
#         f*=j   #此操作一共做1+2+3+4+...+n次
#     s+=f
# print (s)
#重复计算多。比如算3！算了一边，别的会继续
#改进：1*2*3只要算一遍就可以记下来，下次算4！直接用

#方法三：
# n=int(input())
# s,f=0,1
# for i in range (1,n+1):
#     f*=i
#     s+=f
# print(s)

#输入正整数n（n>=2)，求不大于n的全部质数
#方法一：
# n=int(input())
# for i in range (2,n+1):
#     ok=True
#     for k in range (2,i):
#         if i%k==0:
#             ok=False
#             break
#     if ok:
#         print(i)

#方法二：优化
# n=int(input())
# print(2)
# for i in range (3,n+1,2):  #步长为2，只考虑偶数
#     ok=True
#     for k in range (3,i,2):
#         if i%k==0:
#             ok=False
#             break
#         if k*k>i:      #大于根号i的数就不用试了
#             break
#     if ok:
#         print(i)

#求最大跨度值
# n=int(input())
# s=input().split()
# maxV=minV=int(s[0])
# for x in s:
#     if maxV<int(x):
#         maxV=int(x)
#         #minV=min(minV, int(x))      #用Python自带的min，max函数
#     if minV>int(x):
#         minV=int(x)
# print(maxV-minV)

#角谷猜想
# n=int(input())
# while n!=1:
#     if n%2:  #n%2和n%2！=0 等价
#         print(str(n)+"*3+1="+str(n*3+1))
#         n=n*3+1
#     else:
#         print(str(n)+"/2="+str(n//2))
#         n//=2
# print("End")

#统计2出现的次数

# print(__name__) #在Python.exe+文件名称 的情况下，默认是__main__


import struct


#format='<IiiHHIIiiII'
BITMAPINFOHEADER={
    "biSize":0,
    "biWidth":1,
    "biHeight":2,
    "biPlanes":3,
    "biBitCount":4,
    "biCompression":5,
    "biSizeImage":6,
    "biXPelsPerMeter":7,
    "biYPelsPerMeter":8,
    "biClrUsed":9,
    "biClrImportant":10,
}

#format='<BBB'
RGBTRIPLE={
    "rgbtBlue":0,
    "rgbtGreen":1,
    "rgbtRed":2
}

if __name__=="__main__":

    with open('what.bmp','rb') as f:
        fileheader = struct.unpack('<HIHHI',f.read(14))
        infoheader = struct.unpack('<IiiHHIIiiII',f.read(40))

        if fileheader[BITMAPFILEHEADER['bfType']]!=struct.unpack('<H',b'BM')[0]:
            print("wrong file format!",file=sys.stderr)
            sys.exit(2)

        print(fileheader[BITMAPINFOHEADER['bfSize']])
        print(infoheader[BITMAPINFOHEADER['bfHeight']])
        print(infoheader[BITMAPINFOHEADER['bfWidth']])







