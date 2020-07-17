x=int(input())
a=list(map(int,input().split()))
for i in range(1,x):
    a[i]=a[i]+a[i-1]
mi=a[0]
ma=a[-1]
chec=[-1]*(ma-mi+1)
j=0
for i in range(mi,ma+1):
    while j<x and a[j]<i:
        j+=1
    chec[i-mi]=j+1
#print(a)
#print(chec)
for q in range(int(input())):
    n=int(input())
    if n>ma:
        print(-1)
    elif n<mi:
        print(1)
    else:
        print(chec[n-mi])