class UnionFind(object):
    def __init__(self,n):
        self.parent=[-1]*n
        self.ranking=[0]*n
        self.unioncnt=n
        for i in xrange(n):
            self.parent[i]=i
            
    def find(self,x):
        if self.parent[x]==x: return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def connected(self,x,y):
        rtx=self.find(x)
        rty=self.find(y)
        if rtx!=rty:
            if self.ranking[rtx]>self.ranking[rty]:
                self.parent[rty]=rtx
            else:
                self.parent[rtx]=rty
                if self.ranking[rtx]==self.ranking[rty]:
                   self.ranking[rty]+=1
            self.unioncnt-=1
                
    def getcount(self):
        return self.unioncnt
        
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res=0
        row=len(grid)
        if not row: return 0
        col=len(grid[0])
        cntzero=0
        UF=UnionFind(row*col)
        for i in range(row):
            for j in range(col):
               if grid[i][j]=='0':
                   cntzero+=1
                   continue
               if j>0 and grid[i][j]=='1' and grid[i][j-1]=='1':
                   UF.connected(i*col+j,i*col+j-1)
               if i>0 and grid[i][j]=='1' and grid[i-1][j]=='1':
                   UF.connected(i*col+j,(i-1)*col+j)
               if j+1<col and grid[i][j]=='1' and grid[i][j+1]=='1':
                   UF.connected(i*col+j,i*col+j+1)
               if i+1<row and grid[i][j]=='1' and grid[i+1][j]=='1':
                   UF.connected(i*col+j,(i+1)*col+j)
        # 0 companent need be get rid of
        return abs(UF.getcount()-cntzero)
