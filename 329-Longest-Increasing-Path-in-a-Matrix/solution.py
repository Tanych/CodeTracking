class Solution(object):
    def traval(self,dmem,lmem,row,col,i,j):
        pos=i*col+j
        if dmem[pos]==0:return 1
        if lmem[pos]!=-1: return lmem[pos]
        left=right=up=down=0
        if dmem[pos]&0x8:
            left=self.traval(dmem,lmem,row,col,i,j-1)
        if dmem[pos]&0x4:
            right=self.traval(dmem,lmem,row,col,i-1,j)
        if dmem[pos]&0x2:
            up=self.traval(dmem,lmem,row,col,i,j+1)
        if dmem[pos]&0x1:
            down=self.traval(dmem,lmem,row,col,i+1,j)
        lmem[pos]=1+max(left,right,up,down)
        return lmem[pos]
            
        
    def qtreesearch(self,matrix):
        """
        using 4 bit to record the relation between left,up,right,down
        """
        row=len(matrix)
        if not row:
            return 0
        col=len(matrix[0])
        dmem,lmem=[0]*(row*col),[-1]*(row*col)
        curlen=maxlen=0
        
        for i in xrange(row):
            for j in xrange(col):
                val=matrix[i][j]
                if j>0 and matrix[i][j-1]>val:
                    dmem[i*col+j]|=0x8
                if i>0 and matrix[i-1][j]>val:
                    dmem[i*col+j]|=0x4
                if j<col-1 and matrix[i][j+1]>val:
                    dmem[i*col+j]|=0x2
                if i<row-1 and matrix[i+1][j]>val:
                    dmem[i*col+j]|=0x1

        for i in xrange(row):
            for j in xrange(col):
                curlen=self.traval(dmem,lmem,row,col,i,j)
                maxlen=max(curlen,maxlen)
        return maxlen
     
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        return self.qtreesearch(matrix)
        def dfs(i,j):
            if not dp[i][j]:
                val=matrix[i][j]
                dp[i][j]=1+max(dfs(i-1,j) if i-1>=0 and val>matrix[i-1][j] else 0,
                               dfs(i+1,j) if i+1<row and val>matrix[i+1][j] else 0,
                               dfs(i,j-1) if j-1>=0 and val>matrix[i][j-1] else 0,
                               dfs(i,j+1) if j+1<col and val>matrix[i][j+1] else 0)
            return dp[i][j]
         
        if not matrix or not matrix[0]: return 0
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0]*col for i in xrange(row)]
        return max(dfs(x,y) for x in xrange(row) for y in xrange(col))