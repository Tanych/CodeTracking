class UnionFind(object):
    def __init__(self,n):
        self.parents=range(n)
        self.ranks=[0]*n
        self.cnt=n
        
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    
    def united(self,x,y):
        rtx=self.find(x)
        rty=self.find(y)
        if rtx!=rty:
            if self.ranks[rtx]<self.ranks[rtx]:
                self.parents[rtx]=rtx
            else:
                self.parents[rty]=rtx
                if self.ranks[rtx]==self.ranks[rtx]:
                    self.ranks[rtx]+=1
                self.cnt -= 1
                    
    def getcnt(self):
        return self.cnt
        
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n==0: return 0
        UF = UnionFind(n)
        for edge in edges:
            UF.united(edge[0], edge[1])
        return UF.getcnt()
        