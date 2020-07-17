n=int(input())
a=list(map(int,input().split()))
a.sort()
if a[-1]<0:
    print(a[-1],1)
else:
    for i in range(n):
        if a[i]>-1:
            break
    ans=sum(a[i:])
    print(ans,n-i)
