def median(A,N):
    for x in range(1,len(N)):
        N[x]=N[x-1]+N[x]
    m=N[-1]//2 
    i=0
    while m>N[i]:
        #print(i)
        i=i+1
    if m>N[0]:
        m=m-N[i-1]
    if A[i][0]+m-1<=max(A[i]):
        return A[i][0]+m-1
    return A[i+1][0]
def medianright(A,N):
    j=0
    right=N[-1]//2+(N[-1]-N[-1]//2)//2
    #print(right)
    while N[j]<right:
        j+=1 
    if right>N[0]:
        right=right-N[j-1]
    if A[j][0]+right-1<=max(A[j]):
        return A[j][0]+right-1
    return A[j+1][0]
    #return A[j][0]+right-1
def medianleft(A,N):
    left=N[-1]//2-(N[-1]-N[-1]//2)//2
    k=0
    while N[k]<left:
        k+=1 
    if left>N[0]:
        left=left-N[k-1]   
    #print(left,k,N[-1]//2)
    if A[k][0]+left <=max(A[k]):
        return A[k][0]+left
    return A[k+1][0]
n=int(input())
possible=[[1,n]]
N=[n]
while True:
    mid=median(possible,N)
    a=medianright(possible,N)
    b=medianleft(possible,N)
    low=possible[0][0]
    high=possible[-1][1]
    print(mid)
    resp=input()
    if resp=="E":
        break
    if resp=="L":
        print(a)
        resp2=input()
        if resp2=="G":
            #possible=set(possible)
            #y=list(range(mid,a+1))
            #possible=possible-set(y)
            i=0 
            while i<len(possible):
                if possible[i][1]<=a and possible[i][0]>=mid:
                    possible.remove(possible[i])
                    i-=1 
                i+=1
            for i in range(len(possible)):
                if possible[i][0]<mid and possible[i][1]>=a:
                    mmm=possible[i][1]
                    possible[i]=[possible[i][0],mid-1] 
                    if mmm>=a+1:
                        possible=possible[:i+1]+[[a+1,mmm]]+possible[i+1:]
                
                else:
                    if possible[i][1]>mid and possible[i][0]<mid:
                        possible[i]=[possible[i][0],mid-1]
                    elif possible[i][0]<=a and possible[i][1]>a:
                        #kk=possible[i][1]
                        possible[i]=[a+1,possible[i][1]]
            
        if resp2=="L":
            #possible=set(possible)
            #possible=possible-set(list(range(a,high+1)))
            my=0
            while my<len(possible):
                if possible[my][0]>=a:
                    possible.remove(possible[my])
                    my-=1 
                my+=1
            i=0
            while i <len(possible):
                if possible[i][1]>a:
                    possible[i]=[possible[i][0],a-1]
                i+=1
        if resp2=="E":
            break
    if resp=="G":
        print(b)
        resp2=input()
        if resp2=="G":
            #possible=set(possible)
            #possible=possible-set(list(range(low,b+1)))
            i=0
            while i<len(possible):
                if possible[i][1]<=b:
                    possible.remove(possible[i])
                    i-=1
                i+=1
            #print(possible)
            for i in range(len(possible)): 
                if possible[i][1]>b and possible[i][0]<b:
                    #kk=possible[i][1]
                    possible[i]=[b+1,possible[i][1]]
        elif resp2=="L":
            #possible=set(possible)
            #possible=possible-set(list(range(b,mid+1)))
            i=0
            while i <len(possible):
                if possible[i][0]>=b and possible[i][1]<=mid:
                    possible.remove(possible[i])
                    i-=1
                if possible[i][0]>mid:
                    i+=1
                    continue
                if possible[i][0]<b and possible[i][1]>=mid:
                    KK=possible[i][1]
                    possible[i]=[possible[i][0],b-1]
                    if KK>=mid+1:
                        possible.insert(i+1,[mid+1,KK])
                else:
                    if possible[i][0]<mid and possible[i][1]>=mid:
                        possible[i]=[mid+1,possible[i][1]] 
                    elif possible[i][1]>b:
                        if possible[i][0]<=b-1:
                            possible[i]=[possible[i][0],b-1]
                        
                i+=1
        else:
            break
    N=[]
    for i in range(len(possible)):
        N.append(possible[i][1]-possible[i][0]+1)
    #print(possible)
