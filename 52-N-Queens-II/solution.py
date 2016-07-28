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
        
    def dfs(self,bd,n,row,res):
        if row==n:
            res.append(1)
            return
        col=0
        while col!=n:
            if self.checkvalid(bd,row,col,n):
                # the backtracking downtown
                bd[row]=bd[row][:col]+'Q'+bd[row][col+1:]
                self.dfs(bd,n,row+1,res)
                # the backtracking uptown
                bd[row]=bd[row][:col]+'.'+bd[row][col+1:]
            col+=1
                
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # initial the board
        board=['.'*n for _ in xrange(n)]
        res=[]
            
        self.dfs(board,n,0,res)
        return len(res)
        