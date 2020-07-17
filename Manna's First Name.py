for _ in range(int(input())):
    s=input()
    n=len(s)
    c=0
    for i in range(len(s)):
        if i+3<n and s[i:i+4]=="SUVO":
            if i+6<n and s[i:i+7]!="SUVOJIT":
                c+=1
            elif i+6>=n:
                c+=1
    print("SUVO =",c,end="")
    print(", SUVOJIT =",s.count("SUVOJIT"))