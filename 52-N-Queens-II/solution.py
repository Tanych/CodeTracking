class Solution(object):
    def __init__(self):
        self.count=0
        
    def checkvalid(self,borad,row,col,n):
        """
        set board[row][col]=='Q' check whether it's valid result
        """
        # check the above column has 'Q'
        i=0
        while i!=row:
            if borad[i][col]=='Q':
                return False
            i+=1
        # check the left-top 135 and right-top 45
        i,j=row-1,col-1
        while i>=0 and j>=0:
            if borad[i][j]=='Q':
                return False
            i-=1
            j-=1
            
        i,j=row-1,col+1
        while i>=0 and j<n:
            if borad[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
        
                
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # initial the board
        board=[['.' for _ in xrange(n)] for _ in xrange(n)]
        def dfs(borad,n,row):
            if row==n:
                self.count+=1
                return
            for col in xrange(n):
                if self.checkvalid(board,row,col,n):
                    borad[row][col]='Q'
                    dfs(board,n,row+1)
                    borad[row][col]='.'
        dfs(board,n,0)
        return self.count
        