import math
for _ in range(int(input())):
    p,q,r=map(int,input().split())
    a,b,c=map(int,input().split())
    x=[p,q,r]
    y=[a,b,c]
    f1=0
    z1=0
    for i in range(3):
        if x[i]!=y[i]:
            f1+=2**(2-i)
            if x[i]==0:
                z1+=2**(2-i)
    if a==p and b==q and c==r:
        print(0)
    if f1==1 or f1==2 or f1==4:
        print(1)
    if f1==3:
        ans=2
        if q!=0 and r!=0 and b//q==c//r and b%q==0 and c%r==0:
            ans=min(1,ans)
        if  b-q==c-r:
            ans=min(1,ans)
        else:
            ans=min(2,ans)
        print(ans)
    if f1==5:
        ans=2
        if p!=0 and r!=0 and a//p==c//r and a%p==0 and c%r==0:
            ans=min(1,ans)
        if  a-p==c-r:
            ans=min(1,ans)
        else:
            ans=min(2,ans)
        print(ans)
    if f1==6:
        ans=2
        if p!=0 and q!=0 and a//p==b//q and a%p==0 and b%q==0:
            ans=min(1,ans)
        if a-p==b-q:
            ans=min(1,ans)
        else:
            ans=min(2,ans)
        print(ans)
    
    if f1==7:
        ans=3
        # Add -3 , Mul -0
        if a-p==b-q and c-r==b-q:
            ans=min(1,ans)
        if z1==0 and a//p==b//q and b//q==c//r: #Div same
            # Add -0 , Mul- 3
            if a%p==0 and b%q==0 and c%r==0:
                ans=min(1,ans)
            if b%q==c%r and b%q!=0 and a%p==0:
                ans=min(2,ans)
            if a%p==c%r and a%p!=0 and b%q==0:
                ans=min(2,ans)
            if a%p==b%q and a%p!=0 and c%r==0:
                ans=min(2,ans)
            if a%p==b%q==c%r and a%p!=0:
                ans=min(2,ans)
            if (a%p==0 and b%q==0 and c%r!=0) or (a%p!=0 and b%q==0 and c%r==0) and (a%p==0 and b%q!=0 and c%r==0):
                ans=min(2,ans)
        # Add -3 ,Mul*0 - 1
        if a==b and b==c: 
            ans=min(2,ans)
        #Multiplying x - 3 , Add y -3
        if p-q!=0 and q-r!=0 and (a-b)//(p-q)==(b-c)//(q-r) and (b-c)%(q-r)==0 and (a-b)%(p-q)==0: 
            ans=min(2,ans)
        #2 diff same
        if a-p==b-q or b-q==c-r or a-p==c-r:
            ans=min(2,ans)
        # 2 div same
        if p!=0 and q!=0 and a//p==b//q and a%p==0 and b%q==0: 
            ans=min(2,ans)
        if q!=0 and r!=0 and b//q==c//r and b%q==0 and c%r==0: 
            ans=min(2,ans)
        if  r!=0 and p!=0 and c//r==a//p and a%p==0 and c%r==0: 
            ans=min(2,ans)
        # add -2 , mul - 0
        if b-q+a-p==c-r or b-q+c-r==a-p or a-p+c-r==b-q:
            ans=min(2,ans)
        # adding diff to all, Multiplying rem pair
        if (q+a-p)!=0 and (r+a-p)!=0 and b//(q+a-p)==c//(r+a-p) and b%(q+a-p)==0 and c%(r+a-p)==0:
            ans=min(2,ans)
        if (p+b-q)!=0 and r+b-q!=0 and a//(p+b-q)==c//(r+b-q) and a%(p+b-q)==0 and c%(r+b-q)==0:
            ans=min(2,ans)
        if (p+c-r)!=0 and (q+c-r)!=0 and a//(p+c-r)==b//(q+c-r) and a%(p+c-r)==0 and b%(q+c-r)==0 : 
            ans=min(2,ans)
        #adding x to pair, Multiplying y to other pair 
        if r!=0 and (q+a-p)!=0 and b//(q+a-p)==c//r and b%(q+a-p)==0 and c%r==0:
            ans=min(2,ans)
        if q!=0 and (r+a-p)!=0 and b//(q)==c//(r+a-p) and b%(q)==0 and c%(r+a-p)==0:
            ans=min(2,ans)
        if r!=0 and (p+b-q)!=0 and a//(p+b-q)==c//(r) and a%(p+b-q)==0 and c%(r)==0:
            ans=min(2,ans)
        if p!=0 and r+b-q!=0 and a//(p)==c//(r+b-q) and a%(p)==0 and c%(r+b-q)==0:
            ans=min(2,ans)
        if q!=0 and (p+c-r)!=0 and a//(p+c-r)==b//(q) and a%(p+c-r)==0 and b%q==0 :
            ans=min(2,ans)
        if p!=0 and (q+c-r)!=0 and a//(p)==b//(q+c-r) and a%(p)==0 and b%(q+c-r)==0 :
            ans=min(2,ans)
        #Multiplying all and adding to other pair
        if p!=0 and a%p==0 and b-q*(a//p)==c-r*(a//p):
            ans=min(2,ans)
        if q!=0 and b%q==0 and a-p*(b//q)==c-r*(b//q):
            ans=min(2,ans)
        if r!=0 and c%r==0 and a-p*(c//r)==b-q*(c//r):
            ans=min(2,ans)
        # Multiplying 3 and Multiplying 2
        if p!=0 and a%p==0 and (q*(a//p))!=0 and (r*(a//p))!=0 and b//(q*(a//p))==c//(r*(a//p)) and b%(q*(a//p))==0 and c%(r*(a//p))==0:
           ans=min(2,ans)
        if q!=0 and b%q==0 and (p*(b//q))!=0 and (r*(b//q))!=0 and a//(p*(b//q))==c//(r*(b//q)) and a%(p*(b//q))==0 and c%(r*(b//q))==0:
            ans=min(2,ans)
        if r!=0 and c%r==0 and (q*(c//r))!=0 and (p*(c//r))!=0 and a//(p*(c//r))==b//(q*(c//r)) and a%(p*(c//r))==0 and b%(q*(c//r))==0:
            ans=min(2,ans)
        #Multiplying 2 adding 2 
        if p!=0 and a%p==0 and ( b-q*(a//p)==c-r or c-r*(a//p)==b-q):
            ans=min(2,ans)
        if q!=0 and b%q==0 and (a-p*(b//q)==c-r or c-r*(b//q)==a-p):
            ans=min(2,ans)
        if r!=0 and c%r==0 and (a-p*(c//r)==b-q or b-q*(c//r)==a-p):
            ans=min(2,ans)
        # Multiplying 2 and Multiplying 2 
        if p!=0 and r!=0 and a%p==0 and (q*(a//p))!=0 and b//((q*(a//p)))==c//r and c%r==0 and b%(q*(a//p))==0:
            ans=min(2,ans)
        if p!=0 and q!=0 and a%p==0 and (r*(a//p))!=0 and b//q==c//(r*(a//p)) and b%q==0 and c%(r*(a//p))==0:
            ans=min(2,ans) 
        if q!=0 and r!=0 and b%q==0 and (p*(b//q))!=0 and a//(p*(b//q))==c//r and a%(p*(b//q))==0 and c%r==0:
            ans=min(2,ans)
        if q!=0 and p!=0 and  b%q==0  and (r*(b//q))!=0 and a//(p)==c//(r*(b//q)) and a%p==0 and c%(r*(b//q))==0:
            ans=min(2,ans)
        if r!=0 and q!=0 and c%r==0 and (p*(c//r))!=0 and a//(p*(c//r))==b//q and a%(p*(c//r))==0 and b%q==0:
            ans=min(2,ans)
        if r!=0 and p!=0 and c%r==0 and (q*(c//r))!=0 and a//p==b//(q*(c//r)) and a%p==0 and b%(q*(c//r))==0:
            ans=min(2,ans)
        if a-p+b-q==c-r+b-q or b-q+a-p==c-r+a-p or b-q+c-r==a-p+c-r:
            ans=min(2,ans)
        if b-q+c-r==a-p or a-p+c-r==b-q or b-q+a-p==c-r or a-p+b-q==c-r or c-r+a-p==b-q or c-r+b-q==a-p:
            ans=min(2,ans)
        #adding to one pair , Multiplying other
        if p!=0 and q+c-r!=0 and b//(q+c-r)==a//p and a%p==0 and b%(q+c-r)==0:
            ans=min(2,ans)
        if p+c-r!=0 and q!=0 and b//(q)==a//(p+c-r) and a%(p+c-r)==0 and b%q==0:
            ans=min(2,ans)
        if q+a-p!=0 and r!=0 and b//(q+a-p)==c//r and b%(q+a-p)==0 and c%r==0:
            ans=min(2,ans)
        if r+a-p!=0 and q!=0 and b//q==c//(r+a-p) and b%q==0 and c%(r+a-p)==0:
            ans=min(2,ans)
        if p+b-q!=0 and r!=0 and c//r==a//(p+b-q) and c%r==0 and a%(p+b-q)==0:
            ans=min(2,ans)
        if r+b-q!=0 and p!=0 and a//p==c//(r+b-q) and a%p==0 and c%(r+b-q)==0:
            ans=min(2,ans)
        if p!=0 and q!=0 and (b-(c-r))//q==(a-(c-r))//p and (b-(c-r))%q==0 and (a-(c-r))%p==0:
            ans=min(2,ans)
        if q!=0 and r!=0 and (b-(a-p))//q==(c-(a-p))//r and (b-(a-p))%q==0 and (c-(a-p))%r==0:
            ans=min(2,ans)
        if p!=0 and r!=0 and (a-(b-q))//p==(c-(b-q))//r and (a-(b-q))%p==0 and (c-(b-q))%r==0:
            ans=min(2,ans)
        if p!=0 and q!=0 and (b-(c-r))//q==a//p and (b-(c-r))%q==0 and a%p==0:
            ans=min(2,ans)
        if p!=0 and q!=0 and b//q==(a-(c-r))//p and b%q==0 and (a-(c-r))%p==0:
            ans=min(2,ans)
        if q!=0 and r!=0 and (b-(a-p))//q==c//r and (b-(a-p))%q==0 and c%r==0:
            ans=min(2,ans)
        if q!=0 and r!=0 and b//q==(c-(a-p))//r and (b)%q==0 and (c-(a-p))%r==0:
            ans=min(2,ans)    
        if p!=0 and r!=0 and (a-(b-q))//p==c//r and (a-(b-q))%p==0 and c%r==0:
            ans=min(2,ans)
        if p!=0 and r!=0 and a//p==(c-(b-q))//r and a%p==0 and (c-(b-q))%r==0:
            ans=min(2,ans)
        print(ans)