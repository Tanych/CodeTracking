class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # to make the O(n) space 
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
      
        if obstacleGrid[row-1][col-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
                
        dp=[0 for _ in xrange(col)]
        dp[0]=1
        
        # deal with the first row
        for j in xrange(1,col):
            if obstacleGrid[0][j]==1:
                dp[j]=0
            else:
                dp[j]=dp[j-1]
            
        # check the dp[i][j]
        for i in xrange(1,row):
            for j in xrange(0,col):
                if j==0:
                    if obstacleGrid[i][j]==1:
                        dp[j]=0
                else:
                    # if face obstacle, set dp[i][j] to 0
                    if obstacleGrid[i][j]==1:
                        dp[j]=0
                    else:
                        dp[j]=dp[j]+dp[j-1]
                    
        return dp[col-1]
        