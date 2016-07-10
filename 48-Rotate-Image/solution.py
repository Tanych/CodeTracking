class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # every replace it deal with two elelments in one column or row
        row=n/2
        col=n/2
        if n%2!=0:
            col+=1
        for i in xrange(row):
            for j in xrange(col):
                # to remmeber the index just using the case
                tmp=matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=tmp