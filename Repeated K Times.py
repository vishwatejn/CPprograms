n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=dict()
for i in range(n):
    if a[i] in s:
        s[a[i]]+=1
    else:
        s[a[i]]=1
b=[]
for i in s:
    if s[i]==k:
        b.append(i)
print(min(b))