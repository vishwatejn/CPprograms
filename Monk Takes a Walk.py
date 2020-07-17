l=["a","e","i","o","u","A","E","I","O","U"]
for _ in range(int(input())):
    ans=0
    s=input()
    for i in s:
        if i in l:
            ans+=1
    print(ans)