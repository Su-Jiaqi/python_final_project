n=int(input())
if n<0:
    n=-n

lst=[]
while n>1:
    a=n%2
    lst.append(a)
    n=n//2
lst.append(n)
lst_len=len(lst)
if lst_len%8!=0: #如果列表元素个数是8的倍数则不用加零;不是8的倍数则需要补0
    sign=1 #标记(与18行相呼应)
    while sign==1: #只有sign=1时循环才执行
        lst.append(0) #加0
        lst_len=len(lst)
        if lst_len%8==0: #如果加0加到列表长度是8的倍数时就让程序停下来(给sign赋值0,则不满足循环条件,即可退出循环)
             sign=0
lst=lst[ : : -1] #列表倒置
lst=[str(x) for x in lst] #将列表每项元素转为str格式
lst=['one' if k=='1' else k for k in lst] #21-23行,将1变为0,0变为1
lst=['1' if k=='0' else k for k in lst]
lst=['0' if k=='one' else k for k in lst]
lst=' '.join(lst) #将列表所有元素连接为1个字符串
print(lst)

    


   

