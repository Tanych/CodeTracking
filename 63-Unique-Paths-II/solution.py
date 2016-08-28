class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        
        dp=[[0 for _ in xrange(col+1)] for _ in xrange(row+1)]
        dp[0][1]=1
        # check the dp[i][j]
        for i in xrange(1,row+1):
            for j in xrange(1,col+1):
                if obstacleGrid[i-1][j-1]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[row][col]
        