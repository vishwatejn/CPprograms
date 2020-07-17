def solution (A, K):
    ans=0
    for i in A:
        p=[]
        t=[]
        z=0
        for j in range(len(i)):
            if i[j]=="P":
                p=[j]+p
            else:
                t=[j]+t
        while len(p)>0 and len(t)>0:
            if abs(p[-1]-t[-1])<=K:
                ans+=1
                t.pop()
                p.pop()  
            elif p[-1]-t[-1]>K:
                t.pop()
            else:
                p.pop()      
    return ans




T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print (out_)