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
        
        
    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        """
        why the return res is [...], it's doesn't change
        """
        if n<4:
            return []
        
        # initial the board
        board=['.'*n for _ in xrange(n)]
        res=[]
        
        def dfs(bd,n,row):
            if row==n:
                res.append(bd)
                return
            col=0
            while col!=n:
                if self.checkvalid(bd,row,col,n):
                    # the backtracking downtown
                    bd[row]=bd[row][:col]+'Q'+bd[row][col+1:]
                    dfs(bd,n,row+1)
                    # the backtracking uptown
                    bd[row]=bd[row][:col]+'.'+bd[row][col+1:]
                col+=1
            
        dfs(board,n,0)
        return res
        
    def solveNQueens(self, n):
        def dfs(board, row):
            if row == n:
                result.append(['.' * x + 'Q' + '.' * (n - 1 - x) for x in board])
                return
            for x in set_n - set(board):
                # check diagonal conflict
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    dfs(board, row + 1)
                    board[row] = '.'
    
        result, set_n = [], {i for i in xrange(n)}
        dfs(['.'] * n, 0)
        return result
        
        