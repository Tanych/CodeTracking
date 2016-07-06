class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # This is a Brilliant DP solution from morrischen2008
        # It try to record the left and right bounary of the rectange, also the height
        # The max area would be (right-left)*height
        
        row=len(matrix)
        if row==0:
            return 0
            
        col=len(matrix[0])
        if col==0:
            return 0
            
        # left,right bounary of the element and height of the element
        height=[0]*col
        right=[col]*col
        left=[0]*col
        # max area
        maxA=0
        
        for i in xrange(row):
            cur_left=0
            cur_right=col
            # count the height and the left bounary
            for j in xrange(col):
                if matrix[i][j]=='1':
                    height[j]+=1
                    left[j]=max(left[j],cur_left)
                else:
                    height[j]=0
                    left[j]=0
                    cur_left=j+1
            # count the right bounary
            for j in xrange(col-1,-1,-1):
                if matrix[i][j]=='1':
                    right[j]=min(right[j],cur_right)
                else:
                    right[j]=col
                    cur_right=j
                    
            # count the area
            for j in xrange(col):
                maxA=max(maxA,(right[j]-left[j])*height[j])
                
        return maxA
        