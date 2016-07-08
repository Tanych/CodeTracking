class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        
        if row==0:
            return
        # using the first row and first col to record the left matrix
        
        row_first=False
        col_first=False
        
        # first colomn
        for i in xrange(row):
            if matrix[i][0]==0:
                col_first=True
                break
        # fist row
        for j in xrange(col):
            if matrix[0][j]==0:
                row_first=True
                break
        
        # the left part
        for i in xrange(1,row):
            for j in xrange(1,col):
                if matrix[i][j]==0:
                    # using the first row to record
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        # set all the other row to zero
        for i in xrange(1,row):
            if matrix[i][0]==0:
                for j in xrange(1,col):
                    matrix[i][j]=0
        
        # set all the other col to zero
        for j in xrange(1,col):
            if matrix[0][j]==0:
                for i in xrange(1,row):
                    matrix[i][j]=0
        
        # set the first row
        if col_first:
            for i in xrange(row):
                matrix[i][0]=0
        # set the first column
        if row_first:
            for j in xrange(col):
                matrix[0][j]=0
                
