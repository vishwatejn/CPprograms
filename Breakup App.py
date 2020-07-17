a=[0]*32
n=int(input())

for i in range(n):
    s=list(input().split())
    if s[0]=="G:":
        for i in s:
            if i.isdigit():
                a[int(i)]+=2
    else:
        for i in s:
            if i.isdigit():
                a[int(i)]+=1
x=max(a)
y=a.count(x)
if y==1 and a.index(x)==19 or a.index(x)==20:
    print("Date")
else:
    print("No Date")
