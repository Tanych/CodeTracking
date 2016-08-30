class Solution(object):
    def dfssearch(self,grid,i,j, dist, buildingcnt):
        row=len(grid)
        col=len(grid[0])
        visitied = [[False for _ in xrange(col)] for _ in xrange(row)]
        visitied[i][j] = True
        queue = [(i, j, 0)]
        
        while queue:
            i, j, depth = queue.pop(0)
            dist[i][j] = depth if dist[i][j] == 1 << 31 else dist[i][j] + depth
            for newi, newj in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                if 0 <= newi <row and 0 <= newj<col and not visitied[newi][newj]:
                    visitied[newi][newj] = True
                    if grid[newi][newj] == 0:
                        queue.append((newi, newj, depth + 1))
                        buildingcnt[newi][newj] += 1
        
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        if not row: return -1
        col=len(grid[0])
        bcnt=0
        
        dist = [[1 << 31 for _ in xrange(col)] for _ in xrange(row)]
        buildingcnt = [[0 for _ in xrange(col)] for _ in xrange(row)]
        
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j]==1:
                    self.dfssearch(grid,i,j,dist,buildingcnt)
                    bcnt+=1
        mindistance=1<<31
        for i in xrange(row):
            for j in xrange(col):
                if buildingcnt[i][j]==bcnt and dist[i][j] < mindistance:
                    mindistance=dist[i][j]
        return mindistance if mindistance != 1 << 31 else -1
        
        