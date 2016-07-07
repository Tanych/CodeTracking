class Solution(object):
    def dfs(self,board,word,t_idx,row_idx,col_idx):
        if t_idx==len(word):
            return True
        if row_idx<0 or row_idx==len(board) or col_idx<0 or col_idx==len(board[0]):
            return  False
        
        orignal=board[row_idx][col_idx]
        if orignal!=word[t_idx]:
            return False
            
        # make broad[row_idx][col_ids] as visited
        board[row_idx][col_idx]='*'
        # search four dicrection
        res=self.dfs(board,word,t_idx+1,row_idx,col_idx+1) or self.dfs(board,word,t_idx+1,row_idx,col_idx-1) or \
            self.dfs(board,word,t_idx+1,row_idx-1,col_idx) or self.dfs(board,word,t_idx+1,row_idx+1,col_idx)
        # roll back
        board[row_idx][col_idx]=orignal
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row=len(board)
        col=len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                if self.dfs(board,word,0,i,j):
                    return True
        return False
        
        