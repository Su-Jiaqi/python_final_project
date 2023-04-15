'''#1.n!
a=int(input())
b=a
for i in range (a-1,0,-1):
    b*=i  
print(b)'''

#2.计算π的近似值
eps=int(input())
pai_4=0
sign=1
denominator=0
for j in range(0,eps):
    denominator=2*(j+1)-1
    pai_4+=sign*(1/denominator)
    sign=-sign
pai=4*pai_4
print(pai)

'''#3.计算Fibonacci序列的第n项(数列找规律)
F0,F1=0,1
n=int(input())
if n==0:
    output=0
elif n==1:
    output=1
else:
    lst=[0]*(n+1)
    lst[1]=1
    for k in range(2,n+1):
        lst[k]=lst[k-1]+lst[k-2]
    output=lst[n]
print(output)

#4.输入N个整数放在一个列表中，然后从后向前显示列表中的所有元素。
c=list(map(int,input().split()))
c_new=c[ : :-1]
print(c_new)

#5.编写函数，计算列表中整数元素的最大值、最小值和平均值。
d=list(map(int,input().split()))
maxinum=max(d)
mininum=min(d)
averagenum=sum(d)/len(d)
print(maxinum)
print(mininum)
print(averagenum)'''




        
        
