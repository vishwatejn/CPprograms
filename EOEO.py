# cook your dish here
from math import log
for _ in range(int(input())):
    j=int(input())
    if j%2==1:
        print(j//2)
    else:
        if (log(j,2))%1==0:
            print(0)
            continue
        c=0
        ts=j
        while ts%2==0:
            ts=ts//2
            c+=1 
        a=2**(c+1)
        print(j//a)