class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # it's very similar with the Minimum Path Sum #64
        # reduce space to record the previous and current row
        if m>n:
            return self.uniquePaths(n,m)

        curcol=[1 for _ in xrange(n)]
        
        for j in xrange(1,n):
            for i in xrange(1,m):
                curcol[i]=curcol[i]+curcol[i-1]
        
        return curcol[m-1]