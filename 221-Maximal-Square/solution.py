class Solution(object):
    def maximalSquareON(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        row=len(matrix)
        col=len(matrix[0])
        
        cur=[0 for _ in xrange(row+1)]
        
        maxw=pre=0
        for j in xrange(1,col+1):
            for i in xrange(1,row+1):
                tmp=cur[i]
                if matrix[i-1][j-1]=='1':
                    # first choose the smller square between the up and left
                    # it determin the length that [i-1][j-1] can be extend
                    # finally, the square in the [i-2][i-2] also determin 
                    # the dignoal line can be extend
                    cur[i]=min(cur[i-1],cur[i],pre)+1
                    maxw=max(maxw,cur[i])
                else:
                    cur[i]=0
                pre=tmp
                
        return maxw*maxw
        
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        return self.maximalSquareON(matrix)
        
        if not matrix or not matrix[0]:
            return 0
        
        row=len(matrix)
        col=len(matrix[0])
        
        dp=[[0 for _ in xrange(col+1)] for _ in xrange(row+1)]
        
        maxw=0
        for i in xrange(1,row+1):
            for j in xrange(1,col+1):
                if matrix[i-1][j-1]=='1':
                    # first choose the smller square between the up and left
                    # it determin the length that [i-1][j-1] can be extend
                    # finally, the square in the [i-2][i-2] also determin 
                    # the dignoal line can be extend
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                maxw=max(maxw,dp[i][j])
        return maxw*maxw
                
                    