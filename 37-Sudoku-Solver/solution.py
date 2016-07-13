class Solution(object):
    def isValidSudoku(self, board,row,col, ch):
        
        for i in xrange(9):
            if board[i][col]==str(ch):
                return False
        for j in xrange(9):
            if board[row][j]==str(ch):
                return False
        for i in xrange((row/3)*3,(row/3)*3+3):
            for j in xrange((col/3)*3,(col/3)*3+3):
                if board[i][j]==str(ch):
                    return False
        return True
            
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self,board):
        # first try brute force
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j]=='.':
                    for k in xrange(1,10):
                        if self.isValidSudoku(board,i,j,k):
                            board[i]=board[i][:j]+[str(k)]+board[i][j+1:]
                            if self.solve(board):
                                return True
                            else:
                                board[i]=board[i][:j]+['.']+board[i][j+1:]
                    return False
        return True
        
        