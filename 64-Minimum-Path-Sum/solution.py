class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp make things simple 
        # dp[i,j]=min(dp[i-1,j],dp[i,j-1])+grid[i][j]
        # dfs make all things possible that's why the dfs TLE
        
        row=len(grid)
        col=len(grid[0])
        if row==0 or col==0:
            return 0

        dp=[[0 for _ in xrange(col)] for _ in xrange(row)]
        dp[0][0]=grid[0][0]
        # deal the first row
        for i in xrange(1,row):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        # deal the first column
        for j in xrange(1,col):
            dp[0][j]=dp[0][j-1]+grid[0][j]

        for i in xrange(1,row):
            for j in xrange(1,col):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[row-1][col-1]

        
        
        
        