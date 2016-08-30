class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid=[[0 for _ in xrange(n)] for _ in xrange(n)]
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
        if row<0 or row>=self.size or col<0 or col>=self.size:
            return -1
            
        self.grid[row][col]=player
        
        # column
        i=0
        while i<self.size:
            if self.grid[row][i]==player:
                i+=1
            else:
                break
        if i==self.size:
            return player
        
        # row
        i=0
        while i<self.size:
            if self.grid[i][col]==player:
                i+=1
            else:
                break
        if i==self.size:
            return player
        
        # diagonal
        if row==col:
            i=0
            while i<self.size:
                if self.grid[i][i]==player:
                    i+=1
                else:
                    break
            if i==self.size:
                return player
        
        # reverse diagonal     
        if row+col==self.size-1: 
            i=0
            while i<self.size:
                if self.grid[i][self.size-i-1]==player:
                    i+=1
                else:
                    break
            if i==self.size:
                return player
                
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)