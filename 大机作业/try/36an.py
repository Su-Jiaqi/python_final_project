a,n=map(int,input().split())

s=0
for i in range (n):
    s+=a*(10**i)*(n-i)

print(s)