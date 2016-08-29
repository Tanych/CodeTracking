class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row=len(grid)
        if not row: return 0
        col=len(grid[0])
        rowhits,colhits=0,[0]*col
        res=0
        for i in xrange(row):
            for j in xrange(col):
                if j==0 or grid[i][j-1]=='W':
                    rowhits=0
                    k=j
                    while k<col and grid[i][k]!='W':
                        rowhits+=grid[i][k]=='E'
                        k+=1
                if i==0 or grid[i-1][j]=='W':
                    colhits[j]=0
                    k=i
                    while k<row and grid[k][j]!='W':
                        colhits[j]+=grid[k][j]=='E'
                        k+=1    
                if grid[i][j]=='0':
                    res=max(res,rowhits+colhits[j])
        return res
        