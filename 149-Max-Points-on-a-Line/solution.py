# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res=0
        n=len(points)
        # input case
        if n==0:
            return 0
        if n<2:
            return 1
            
        # normal
        for i in xrange(n):
            khash={}
            # deal with two edge case duplicates and a.x==b.x
            dupcnt,vercnt=0,0
            for j in xrange(i+1,n):
                # separate the vertical count and duplicates
                if points[i].x-points[j].x==0:
                    if points[i].y==points[j].y:
                        dupcnt+=1
                    else:
                        vercnt+=1
                else:
                    k=float(points[i].y-points[j].y)/float(points[i].x-points[j].x)
                    khash[k]=khash.get(k,0)+1
            # get the count with max slope
            slopemax=max(khash.values()) if khash else 0    
            # get the max number on one line
            maxOnline=max(slopemax,vercnt)+dupcnt
            # update results
            res=max(res,maxOnline)
        # 1 is the start point to count
        return res+1
                    