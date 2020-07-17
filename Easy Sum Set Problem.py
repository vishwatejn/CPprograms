n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=list(map(int,input().split()))

ans=[]
x=c[-1]-a[-1]
for i in range(x,-1,-1):
    if all(i+j in c for j in a) :
        ans.append(i)
ans=ans[::-1]
print(*ans) 
