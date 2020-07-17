ans=0
for i in range(int(input())):
    a,b=map(int,input().split())
    r=a/b
    x=b/a
    if r>=1.60 and r<=1.70:
        ans+=1
    elif x>=1.60 and x<=1.70:
        ans+=1
print(ans)