class BinaryIndexTree(object):
    def __init__(self,n):
        self.array=[0]*(n+1)
        self.size=n

    def lowbit(self,idx):
        return idx&(-idx)
        
    def updatebit(self,idx,val):
        idx+=1
        while idx<=self.size:
            self.array[idx]+=val
            idx+=self.lowbit(idx)

    def sumarr(self,idx):
        res=0
        idx+=1
        while idx>0:
            res+=self.array[idx]
            idx-=self.lowbit(idx)
        return res
    
    def sumrange(self,x,y):
        return self.sumarr(y)-self.sumarr(x)

    def printitem(self):
        print self.array[1:]
        
class BinaryIndexTree2D(object):
    def __init__(self,n):
        self.trees=[None]*n
        self.treecnt=n
        
    def construct(self,x,vals):
        tree=BinaryIndexTree(len(vals))
        for i in xrange(len(vals)):
            tree.updatebit(i,vals[i])
        self.trees[x]=tree
        
    def update(self,x,y,val):
        if self.trees[x]:
            self.trees[x].updatebit(y,val)

    def sumrange(self,x1,y1,x2,y2):
        res=0
        for i in xrange(x1,x2+1):
            if self.trees[i]:
                res+=self.trees[i].sumrange(y1-1,y2)
        return res
    
    def printitems(self):
        for i in xrange(self.treecnt):
            self.trees[i].printitem()

class Solution(object):
    def __init__(self,matrix):
        self.bintree2d=BinaryIndexTree2D(len(matrix))
        for i in xrange(len(matrix)):
            self.bintree2d.construct(i,matrix[i])
        
    def update(self,x,y,val):
        self.bintree2d.update(x,y,val)
        
    def sumRegion(self,x1,y1,x2,y2):
        return self.bintree2d.sumrange(x1,y1,x2,y2)
    
    def printitems(self):
        self.bintree2d.printitems()

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
t=Solution(matrix)
t.printitems()
print t.sumRegion(2, 1, 4, 3)
t.update(3, 2, 2)
print t.sumRegion(2, 1, 4, 3)
                
            
