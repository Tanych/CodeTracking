class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:
            return []
        matrix=[[0 for _ in xrange(n)] for _ in xrange(n)]
        
        # using i,j to record the pos
        i=j=0
        total=n*n
        start=1
        matrix[0][0]=1
        while start<total:
            while j+1<n and matrix[i][j+1]==0:
                start+=1
                matrix[i][j+1]=start
                j+=1
               
            while i+1<n and matrix[i+1][j]==0:
                start+=1
                matrix[i+1][j]=start
                i+=1
                
            while j-1>=0 and matrix[i][j-1]==0:
                start+=1
                matrix[i][j-1]=start
                j-=1
                
            while i-1>=0 and matrix[i-1][j]==0:
                start+=1
                matrix[i-1][j]=start
                i-=1
               
        
        return matrix
        