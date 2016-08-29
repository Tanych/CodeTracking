class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
            
        positions=set()
        sumk=0
        for p in points:
            positions.add((p[0],p[1]))
            
        # avoid duplicate points
        for p in positions:
            sumk+=p[0]
        pivot=float(sumk)/float(len(positions))
        for p in positions:
            if (int(2*pivot-p[0]),p[1]) not in positions:
                return False
        return True
        