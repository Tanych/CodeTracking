class UnionFind(object):
    def __init__(self,n):
        self.parent=range(n)
        self.rank=[0]*n
        # record how many has been united
        self.cnt=n
        
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def united(self,x,y):
        rtx=self.find(x)
        rty=self.find(y)
        if rtx!=rty:
            if self.rank[rtx]<self.rank[rty]:
                self.parent[rtx]=rty
            else:
                self.parent[rty]=rtx
                if self.rank[x]==self.rank[y]:
                    self.rank[x]+=1
            self.cnt-=1
            return False
        return True
            
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # for the undirect graph, topologic sort
        # might has problem when edges are [1,0],[2,0]
        # now tends to UF
        UF=UnionFind(n)
        for e in edges:
            if UF.united(e[0],e[1]):
                return False
        return UF.cnt==1
                
        