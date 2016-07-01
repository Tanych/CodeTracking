class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # directly update triangle
        for i in xrange(1,len(triangle)):
            # [i][0]->[i-1][0]
            triangle[i][0]+=triangle[i-1][0]
            # [i][n-1]->[i-1][n-1]
            triangle[i][-1]+=triangle[i-1][-1]
            # the row i length is i+1
            for j in xrange(1,i):
                triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        # return min in last row
        return min(triangle[-1])
            