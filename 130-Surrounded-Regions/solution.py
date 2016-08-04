class UnionFind(object):
    def __init__(self,n):
        self.parent=[-1]*n
        self.rank=[0]*n
        self.union=0
        for i in xrange(n):
            self.parent[i]=i
    
    def find(self,x):
        if self.parent[x]==x: return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def unionxy(self,x,y):
        # don't use union to define the function name
        # it cause a problem
        rx=self.find(x)
        ry=self.find(y)
        if rx!=ry:
            if self.rank[rx]>self.rank[ry]:
                self.parent[ry]=rx
            else:
                self.parent[rx]=ry
                if self.rank[rx]==self.rank[ry]:
                    self.rank[ry]+=1
            self.union+=1
            
    def isunion(self,x,y):
        return self.find(x)==self.find(y)
    
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        The union find mani iead is to connect the boundary `O` to a dumpy node
        and then connect all the neighors to the dumpy, finally replace all the 
        node 'O' outside the dumpy
        
        """
        row=len(board)
        if not row:
            return 
        col=len(board[0])
        UF=UnionFind(row*col+1)
        for i in xrange(row):
            for j in xrange(col):
                if (i==0 or i==row-1 or j==0 or j==col-1) and board[i][j]=='O':
                    UF.unionxy(col*i+j,row*col)
                elif board[i][j]=='O':
                    if board[i-1][j]=='O':
                        UF.unionxy(col*(i-1)+j,i*col+j)
                    if board[i+1][j]=='O':
                        UF.unionxy(col*(i+1)+j,i*col+j)
                    if board[i][j+1]=='O':
                        UF.unionxy(col*i+j+1,i*col+j)
                    if board[i][j-1]=='O':
                        UF.unionxy(col*i+j-1,i*col+j)
        
        # replace
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j]=='O' and not UF.isunion(i*col+j,row*col):
                    board[i][j]='X'
        
    