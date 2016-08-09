class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m=len(matrix)
        n=len(matrix[0])
        
        return self.helper(matrix,0,n-1,0,m-1,target)
        
    def helper(self,matrix,left,right,top,bottom,target):
        if left>right or top>bottom:
            return False
        
        l,r,t,b=left,right,top,bottom
        
        while l<=r and t<=b:
            midx,midy=(l+r)/2,(t+b)/2
            
            if matrix[midy][midx]<target:
                l=midx+1
                t=midy+1
            elif matrix[midy][midx]>target:
                r=midx-1
                b=midy-1
            else:
                return True
        # search the 2 and 3 section
        return self.helper(matrix,l,right,top,b,target) or self.helper(matrix,left,r,t,bottom,target)
        