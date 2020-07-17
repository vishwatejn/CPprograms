# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if a[i]>k:
            ans+=a[i]-k
    print(ans)