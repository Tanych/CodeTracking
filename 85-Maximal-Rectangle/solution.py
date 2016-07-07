class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # this method reflects the maximal histogram rect
        # using the stack the record the highest height in previous 
        
        height=[0 for _ in xrange(len(matrix[0]))] if matrix else None
        # record the height
      
        maxA=0
        for row in matrix:
            stack=[]
            # get the height record for each row
            for cnt,ch in enumerate(row):
                height[cnt]=(height[cnt]+1) if ch=='1' else 0
            # get the max area in each row
            for idx,ht in enumerate(height+[0]):
                # count the area util the stack is the heighest
                # pay attention to the while. it will continue count 
                # until it stops at the height large than the new one
                while stack and ht<height[stack[-1]]:
                    th=height[stack.pop()]
                    # count the max area
                    maxA=max(maxA,th*(idx-stack[-1]-1 if stack else idx))
                stack.append(idx)
        return maxA