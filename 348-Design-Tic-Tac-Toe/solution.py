class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows=[0]*n
        self.cols=[0]*n
        self.digal=self.revdigal=0
        self.size=n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add=1 if player==1 else -1
        self.rows[row]+=add
        self.cols[col]+=add
        self.digal+=add if row==col else 0
        self.revdigal+=add if row+col==self.size-1 else 0
        if abs(self.rows[row])==self.size or abs(self.cols[col])==self.size \
            or abs(self.digal)==self.size or abs(self.revdigal)==self.size:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)