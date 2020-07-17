# cook your dish here
def vtsolve(n) : 
    for i in range(0, n) : 
        for j in range(0, n) : 
            x = min(min(i, j), min(n-1-i, n-1-j)) 
            if (i <= j) : 
                print((n-2*x) * (n-2*x)-(i-x)- (j-x), end = " ") 
            else : 
                print(((n-2*x-2)*(n-2*x-2) +(i-x) + (j-x)), end=" ") 
        print() 
for _ in range(int(input())):
    n=int(input())
    vtsolve(n)
    