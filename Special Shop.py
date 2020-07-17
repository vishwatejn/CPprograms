for _ in range(int(input())):
    n,a,b=map(int,input().split())
    i=round((b*n)/(a+b))
    print(a*(i**2)+b*((n-i)**2))