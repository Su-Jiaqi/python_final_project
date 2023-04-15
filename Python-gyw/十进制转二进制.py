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
if lst_len%8!=0:
    sign=1
    while sign==1:
        lst.append(0)
        lst_len=len(lst)
        if lst_len%8==0:
             sign=0
lst=lst[ : : -1]
lst=[str(x) for x in lst]
lst=['one' if k=='1' else k for k in lst]
lst=['1' if k=='0' else k for k in lst]
lst=['0' if k=='one' else k for k in lst]
lst=' '.join(lst)
print(lst)

    


   

