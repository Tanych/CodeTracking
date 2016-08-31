class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.row=len(matrix)
        if self.row==0: return
        self.col=len(matrix[0])
        self.bintree2d=[[0 for _ in xrange(self.col+1)] for _ in xrange(self.row+1)]
        self.nums=[[0 for _ in xrange(self.col)] for _ in xrange(self.row)]
        
        for i in xrange(self.row):
            for j in xrange(self.col):
                self.update(i,j,matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.row==0 or self.col==0:
            return 
        diff=val-self.nums[row][col]
        self.nums[row][col]=val
        i=row+1
        while i<self.row+1:
            j=col+1
            while j<self.col+1:
                self.bintree2d[i][j]+=diff
                j+=j&(-j)
            i+=i&(-i)
            
    def sumrange(self,row,col):
        sumres=0
        i=row
        while i>0:
            j=col
            while j>0:
                sumres+=self.bintree2d[i][j]
                j-=j&(-j)
            i-=i&(-i)
        return sumres
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.row==0 or self.col==0:
            return 0
        return self.sumrange(row2+1,col2+1)+self.sumrange(row1,col1)-\
            self.sumrange(row1,col2+1)-self.sumrange(row2+1,col1)
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)