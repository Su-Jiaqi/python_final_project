#定义函数,计算整数部分
def integer_cal(n):
    if n<0: #n为负数的情况
        n=-n

        lst=[]
        while n>1:
            a=n%2
            lst.append(a)
            n=n//2
        lst.append(n)
        lst_len=len(lst)
        if lst_len%8!=0: #如果列表元素个数是8的倍数则不用加零;不是8的倍数则需要补0
            num_add=8-lst_len%8
            for k in range(0,num_add): #添加除以8所得余数个0
                m=int(0)
                lst.append(m)

        lst=lst[ : : -1] #列表倒置
        lst=['one' if k==1 else k for k in lst] #19-21行,将1变为0,0变为1
        lst=[1 if k==0 else k for k in lst]
        lst=[0 if k=='one' else k for k in lst]

        #25-34行,二进制+1过程
        for i in range(len(lst)-1,-1,-1): 
            if i==len(lst)-1:
                lst[i]+=1
            if lst[i]==2: #如果出现2就变0,下一位进位
                lst[i]=0
                if i>0:
                    lst[i-1]+=1
                else: #如果最后一位也需要进位则需添加一项
                    n=int(1)
                    lst.insert(0,n) #insert函数,向列表头部添加元素
        return lst
    
    elif n>0: #n为正数的情况
        if n==1:
            part_integer=[1]
        else:
            lst_1=[]
            while n>1:
                a=n%2
                lst_1.append(a)
                n=n//2
            lst_1.append(n)
            lst_1=lst_1[ : : -1]
            return lst_1
           
    elif n==0: #n为0的情况
        lst_2=[0]
        return lst_2

#定义函数,计算小数部分
def decimal_cal(m):
    b=1
    lst2 = []
    while b<=4: #循环精度为4
        m=m*2
        if m>=1:
            lst2.append(1)
            m=m-1
        else:
            lst2.append(0)
        b+=1
    return lst2

Input=float(input()) #输入任意有理数

#x为实数的整数部分,y为小数部分
if Input>0:
    x=int(Input)
    y=Input-x
elif Input<0:
    x=int(Input)
    y=x-Input
else:
    x=0
    y=0

lst_integer=integer_cal(x) #调用函数,计算整数部分
lst_decimal=decimal_cal(y) #调用函数,计算小数部分
lst_all=[]

#合并整数和小数
for i in lst_integer:
    lst_all.append(i)
lst_all.append('.')
for j in lst_decimal:
    lst_all.append(j)
lst_all=' '.join(map(str,lst_all))
print(lst_all)



    




    
