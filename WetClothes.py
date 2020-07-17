n,m,g = map(int,input().split())
r = list(map(int,input().split()))
d = list(map(int,input().split()))
dif =[]
for i in range(len(r)-1):
    x = r[i+1]-r[i]
    dif.append(x)
x = max(dif)
c = 0
for i in range(len(d)):
    if d[i] <= x:
        c += 1
print(c)