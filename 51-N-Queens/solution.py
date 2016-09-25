class Solution(object):
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
        
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[['.' for _ in xrange(n)] for _ in xrange(n)]
        res=[]
        def dfs(bd,n,row):
            if row==n:
                res.append([''.join(row) for row in bd])
                return
            for col in xrange(n):
                if self.checkvalid(bd,row,col,n):
                    bd[row][col]='Q'
                    dfs(bd,n,row+1)
                    bd[row][col]='.'
        dfs(board,n,0)
        return res
        
        