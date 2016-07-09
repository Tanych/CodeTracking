class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        
        dp=[[1 for _ in xrange(col)] for _ in xrange(row)]
        
        # if check the `1` in the first row, the right all set 0
        for i in xrange(row):
            if obstacleGrid[i][0]==1:
                for k in xrange(i,row):
                    dp[k][0]=0
                break
        # if check one `1` in the first column the bottom next set 0
        for j in xrange(col):
             if obstacleGrid[0][j]==1:
                for k in xrange(j,col):
                    dp[0][k]=0
                break
        
        # check the dp[i][j]
        for i in xrange(1,row):
            for j in xrange(1,col):
                # if face obstacle, set dp[i][j] to 0
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
        return dp[row-1][col-1]
        