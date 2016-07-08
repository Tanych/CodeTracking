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
        # but using two col, the swap might cost lots of time
        # reduce to one list
        row=len(grid)
        col=len(grid[0])
        if row==0 or col==0:
            return 0
     
        curcol=[grid[0][0] for _ in xrange(row)]
        
        # deal the first row
        for i in xrange(1,row):
            curcol[i]=curcol[i-1]+grid[i][0]

        for j in xrange(1,col):
            # the precol can replaced by using the value before updated
            curcol[0]=curcol[0]+grid[0][j]
            for i in xrange(1,row):
                curcol[i]=min(curcol[i-1],curcol[i])+grid[i][j]
            # update the previous using current value and then move on
            # since the curcol will update in the next loop
           
            
        return curcol[row-1]

        
        
        
        