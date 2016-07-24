class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.dp=None
        if not matrix or not matrix[0]:
            return
        
        row=len(matrix)
        col=len(matrix[0])
        
        self.dp=[[0 for _ in xrange(col+1)] for _ in xrange(row+1)]
        
        for i in xrange(1,row+1):
            for j in xrange(1,col+1):
                sumcol=sum(matrix[x][j-1] for x in xrange(i-1))
                sumrow=sum(matrix[i-1][x] for x in xrange(j-1))
                self.dp[i][j]=sumcol+sumrow+matrix[i-1][j-1]+self.dp[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.dp:
            return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
        else:
            return 0
    


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)