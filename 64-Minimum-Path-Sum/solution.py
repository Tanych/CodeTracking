class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp make things simple 
        # dp[i,j]=min(dp[i-1,j],dp[i,j-1])+grid[i][j]
        # dfs make all things possible that's why the dfs TLE
        
        # reduce the record space,
        # we only need record the previous column and current column
        row=len(grid)
        col=len(grid[0])
        if row==0 or col==0:
            return 0
        precol=[grid[0][0] for _ in xrange(row)]
        curcol=[0 for _ in xrange(row)]
        
        # deal the first row
        for i in xrange(1,row):
            precol[i]=precol[i-1]+grid[i][0]

        for j in xrange(1,col):
            # current column is == precol+grid[0][j]
            # precol[0] is updated by replace
            curcol[0]=precol[0]+grid[0][j]
            for i in xrange(1,row):
                curcol[i]=min(curcol[i-1],precol[i])+grid[i][j]
            # update the previous using current value and then move on
            # since the curcol will update in the next loop
            precol,curcol=curcol,precol
            
        return precol[row-1]

        
        
        
        