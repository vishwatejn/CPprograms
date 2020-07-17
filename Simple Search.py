n=int(input())
a=list(map(int,input().split()))
k=int(input())
try:
    print(a.index(k))
except:
    print(-1)