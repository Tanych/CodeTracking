class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=len(board)
        col=len(board[0])
        
        if row!=9 or col!=9:
            return False
        
        # using the moving num to record the occur of nums
        # 3 rules for check sudoku
        trows,tcols,blocks=[0]*9,[0]*9,[0]*9
        idx=0
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j]!='.':
                    if not board[i][j].isdigit():
                        return False
                        
                    idx=1<<int(board[i][j])
                    # check whether has the same value in the same row col block
                    if trows[i]&idx or tcols[j]&idx or blocks[(i/3)*3+j/3]&idx:
                        return False
                        
                    trows[i]|=idx
                    tcols[j]|=idx
                    # i=8 j=8, block[9]
                    # i=4 j=8, block[2]
                    blocks[(i/3)*3+j/3]|=idx
                
        return True
        