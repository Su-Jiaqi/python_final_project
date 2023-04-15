n=int(input())
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

    #24-33行,二进制+1过程
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

    lst=[str(x) for x in lst]
    lst=' '.join(lst) #将列表所有元素连接为1个字符串
    print(lst)

elif n>0: #n为正数的情况
    if n==1:
        print(str(1))
    else:
        lst_=[]
        while n>1:
            a=n%2
            lst_.append(a)
            n=n//2
        lst_.append(n)
        lst_=lst_[ : : -1]
        lst_=' '.join(map(str,lst_))
        print(lst_)

elif n==0: #n为0的情况
    print(str(0))
    



    


   

