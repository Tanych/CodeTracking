class Solution(object):
    def search(self,board,i,j,row,col):
        if board[i][j]=='O':
            board[i][j]='#'
            # get rid of the four boundary
            if i>1:
                self.search(board,i-1,j,row,col)
            if i<row-1:
                self.search(board,i+1,j,row,col)
            if j>1:
                self.search(board,i,j-1,row,col)
            if j<col-1:
                self.search(board,i,j+1,row,col)
                
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # a very straight forward way is check the bounary whether they has O
        # if has update all the neighor with another value
        # and then update all the left O to X, after that rollback the update value
        row=len(board)
        if row==0:
            return
        
        col=len(board[0])
        
        # check the first and last colum
        for i in xrange(row):
            # first column
            self.search(board,i,0,row,col)
            # last column
            if col>1:
                self.search(board,i,col-1,row,col)
        
        # check the first and last row
        for j in xrange(col):
            self.search(board,0,j,row,col)
            if row>1:
                self.search(board,row-1,j,row,col)
        
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j]=='O':
                     board[i][j]='X'
                     
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j]=='#':
                     board[i][j]='O'
        