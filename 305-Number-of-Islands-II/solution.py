class UnionFind(object):
    def __init__(self,n):
        self.parent=[-1]*n
        self.rank=[0]*n
        # record how many has been united
        self.cnt=0
        
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
            self.cnt+=1
    
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        UF=UnionFind(m*n)
        res=[]
        for i,(r,c) in enumerate(positions):
            UF.parent[r*n+c]=r*n+c
            for newi,newj in (r,c+1),(r,c-1),(r-1,c),(r+1,c):
                if 0<=newi<m and 0<=newj<n and UF.parent[newi*n+newj]!=-1:
                    UF.united(r*n+c,newi*n+newj)
            # the number of 1 minus the united number
            res.append(i+1-UF.cnt)
        return res
        