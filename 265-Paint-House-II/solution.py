class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        row=len(costs)
        if not row: return 0
        col=len(costs[0])
        premin=presec=0
        preidx=-1
        for i in xrange(row):
            curmin=cursec=1<<31
            curidx=-1
            for j in xrange(col):
                diff=presec if preidx==j else premin
                costs[i][j]=costs[i][j]+diff
                # update curmin and cur second min
                # if less than curmin move two
                if costs[i][j]<curmin:
                    cursec=curmin
                    curmin=costs[i][j]
                    curidx=j
                # if less than one move the second
                elif costs[i][j]<cursec:
                    cursec=costs[i][j]
            presec=cursec
            premin=curmin
            preidx=curidx
            
        return curmin
                    