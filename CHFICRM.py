# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=dict()
    b[5]=0
    b[10]=0 
    b[15]=0 
    flag=0
    for i in range(n):
        if a[i]==5:
            b[5]+=1
        elif a[i]==10:
            if b[5]>0:
                b[10]+=1 
                b[5]-=1
            else:
                flag=1
                break
        else:
            if b[10]>0:
                b[10]-=1 
            elif b[5]>1:
                b[5]-=2
            else:
                flag=1 
                break
    if flag==1:
        print("NO")
    else:
        print("YES")