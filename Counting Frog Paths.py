x,y,s,T=map(int,input().split())
ans=0
for i in range(x,x+s+1):
    j=y
    while i+j<=T and j<y+s+1:
        ans+=1
        j+=1
print(ans)