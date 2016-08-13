class Solution(object):
    def __init__(self):
        self.trow=[0]*9
        self.tcol=[0]*9
        self.block=[0]*9
    
    def initstate(self,board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j]!='.':
                   self.setstate(board,i,j)
                    
    def setstate(self,board,i,j):
        idx=1<<int(board[i][j])
        self.trow[i]|=idx
        self.tcol[j]|=idx
        self.block[(i/3)*3+(j/3)]|=idx
        
    def unsetstate(self,board,i,j):
        idx=1<<int(board[i][j])
        self.trow[i]&=~idx
        self.tcol[j]&=~idx
        self.block[(i/3)*3+(j/3)]&=~idx
    
    def isValidSudoku(self,board,i,j):
        idx=1<<int(board[i][j])
        if self.trow[i]&idx or self.tcol[j]&idx or self.block[(i/3)*3+(j/3)]&idx:
            return False
        return True
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.initstate(board)
        self.dfssolve(board,0,0)
        
    def dfssolve(self,board,i,j):
        if i>8:
            return True
        if j>8:
            return self.dfssolve(board,i+1,0)
                
        if board[i][j]=='.':
            for k in xrange(1,10):
                board[i][j]=str(k)
                if self.isValidSudoku(board,i,j):
                    self.setstate(board,i,j)
                    if self.dfssolve(board,i,j+1):
                        return True
                    self.unsetstate(board,i,j)
                
            board[i][j]='.'
            return False
        else:
            return self.dfssolve(board,i,j+1)
        