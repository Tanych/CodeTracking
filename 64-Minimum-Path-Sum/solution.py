class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        if row==0 or col==0:
            return 0
        currow=[grid[0][0] for _ in xrange(col)]
        # deal the first row
        for j in xrange(1,col):
            currow[j]=currow[j-1]+grid[0][j]

        for i in xrange(1,row):
            # the precol can replaced by using the value before updated
            currow[0]=currow[0]+grid[i][0]
            for j in xrange(1,col):
                currow[j]=min(currow[j-1],currow[j])+grid[i][j]
        return currow[col-1]

        
        
        
        