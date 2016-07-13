class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # 1. check the row, no duplicate nums
        row=len(board)
        col=len(board[0])
        
        for i in xrange(row):
            trow=[]
            for j in xrange(col):
                if board[i][j] in trow:
                    return False
                if board[i][j]!='.':
                    if board[i][j].isdigit():
                        trow.append(board[i][j])
                    else:
                        return False
        # 2. check the column, no duplicate nums             
        for j in xrange(col):
            tcol=[]
            for i in xrange(row):
                if board[i][j] in tcol:
                    return False
                if board[i][j]!='.':
                    if board[i][j].isdigit():
                        tcol.append(board[i][j])
                    else:
                        return False
        
        # 3. check the mini 9 square
        for m in xrange(3):
            for n in xrange(3):
                tsquare=[]
                for i in xrange(3*m,3*(m+1)):
                    for j in xrange(3*n,3*(n+1)):
                        if board[i][j] in tsquare:
                            return False
                        if board[i][j]!='.':
                            if board[i][j].isdigit():
                                tsquare.append(board[i][j])
                            else:
                                return False
        return True
        