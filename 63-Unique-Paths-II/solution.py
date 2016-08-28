class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row,col=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[0 for _ in xrange(col+1)]
        dp[0]=1
        for j in xrange(1,col+1):
            if not obstacleGrid[0][j-1]:
                dp[j]=dp[j-1]
            else:
                break
        # check the dp[i][j]
        for i in xrange(1,row):
            dp[0]=0
            for j in xrange(1,col+1):
                if obstacleGrid[i][j-1]==0:
                    dp[j]=dp[j-1]+dp[j]
                else:
                    dp[j]=0
        return dp[col]
        