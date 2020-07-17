#import time
#start_time = time.time()
def withinpolygon(polygon, point):
    x=len(polygon)
    D=[]
    for i in range(x):
        a1 = polygon[i]
        a2 = polygon[(i + 1) %x]
        q = a2[0]-a1[0]
        p = -(a2[1]-a1[1])
        r = -(p*a1[0] + q*a1[1])
        m = p*point[0] + q*point[1] + r
        D.append(m)
    return all(y> 0 for y in D) or all(y < 0 for y in D)
from functools import reduce
def JarvisHull(points):
    def compare(a, b):
        return (a > b) - (a < b)
    def direction(p, q, r):
        return compare((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]),0)
    turnright = -1
    def movingleft(hull, kl):
        while len(hull) > 1 and direction(hull[-2], hull[-1], kl) == turnright:
            hull.pop()
        if not len(hull) or hull[-1] != kl:
            hull.append(kl)
        return hull
    onedir = reduce(movingleft, points, [])
    otherdir = reduce(movingleft, points[::-1], [])
    otherdir=otherdir[1:-1]
    return onedir+otherdir or onedir
    
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=set()
    for i in range(n):
        x,y=map(int,input().split())
        a.add((x,y))
    hull=[]
    mm=[]
    a=sorted(a)
    while len(a)>2:
        z=JarvisHull(a)
        a=[ele for ele in a if ele not in z]
        minx=z[0][0]
        miny=z[0][1]
        maxx=z[0][0]
        maxy=z[0][1]
        for i in z:
            if i[0]<minx:
                minx=i[0]
            if i[0]>maxx:
                maxx=i[0]
            if i[1]>maxy:
                maxy=i[1]
            if i[1]<miny:
                miny=i[1]
        mm.append([minx,maxx,miny,maxy])
        hull.append(z)
    for i in range(q):
        x,y=map(int,input().split())
        query=[x,y]
        ans=0
        for i in range(len(hull)):
            if query[0]<mm[i][0] or query[0]>mm[i][1] or query[1]<mm[i][2] or query[1]>mm[i][3]:
                break
            elif withinpolygon(hull[i],query):
                ans+=1
            else:
                break
        print(ans)
#print("--- %s seconds ---" % (time.time() - start_time))
