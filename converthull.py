import math
class converthull(object):
    def distance(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))
    def mutilply(self,p1,p2,p0):
        # mutiply>0 then <p0,p1> is on <p0,p2> clockwise
        # <0 is counter clockwise
        return (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
    
    def graham_scan(self,points):
        stck=[]
        k=0
        for i in xrange(1,len(points)):
            if points[i][1]<points[k][1] or \
                (points[i][1]==points[k][1] and points[i][0]<points[k][0]):
                k=i
        # get the leftmost points
        points[0],points[k]=points[k],points[0]
        stck.append(points[0])

        #sorted(points,cmp=lambda x,y:self.distance(stck[-1],x)-self.distance(stck[-1],y) if self.mutilply(x,y,stck[-1])==0 else -self.mutilply(x,y,stck[-1]))
        for i in xrange(1,len(points)):
            k=i
            for j in xrange(i+1,len(points)):
                x,y=points[j],points[k]            
                if self.mutilply(x,y,stck[-1])>0 or \
                   (self.mutilply(x,y,stck[-1])==0 and self.distance(stck[-1],x)<self.distance(stck[-1],y)):
                    k=j
            points[i],points[k]=points[k],points[i]
        
        stck.append(points[1])
        stck.append(points[2])

        for i in xrange(3,len(points)):
            while self.mutilply(points[i],stck[-1],stck[-2])>=0:
               stck.pop()
            stck.append(points[i])
        return stck
t=converthull()
points=[(0,0),(1,2),(1,3),(5,5)]
print t.graham_scan(points)
        
