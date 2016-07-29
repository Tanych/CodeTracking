class Solution(object):
    def dfs(self,board,word,idx,i,j):
        if idx==len(word):
            return True
        # corner
        if i<0 or i==len(board) or j<0 or j==len(board[0]):
            return  False
            
        original=board[i][j]
        # if not prefix not equal
        if original!=word[idx]:
            return False
            
        # move down
        board[i][j]='*'
        res=self.dfs(board,word,idx+1,i,j-1) or self.dfs(board,word,idx+1,i,j+1) or\
            self.dfs(board,word,idx+1,i-1,j) or self.dfs(board,word,idx+1,i+1,j)
        # move uptown
        board[i][j]=original
        return res
        
    def isexist(self,board,word):
        row=len(board)
        col=len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                if self.dfs(board,word,0,i,j):
                    return True
        return False
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for word in set(words):
            if self.isexist(board,word):
                res.append(word)
        return res
        