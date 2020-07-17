for _ in range(int(input())):
    s=input()
    i=0
    n=len(s)
    ans=0
    while i<n:
        if i+1<n and s[i]!=s[i+1]:
            ans+=1 
            i+=2
        else:
            i+=1
    print(ans)