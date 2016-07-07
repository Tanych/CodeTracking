class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # it will the same thought as the #85
        stack=[]
        maxA=0
        for idx,ht in enumerate(heights+[0]):
            while stack and ht<heights[stack[-1]]:
                th=heights[stack.pop()]
                maxA=max(maxA,th*((idx-stack[-1]-1) if stack else idx))
            stack.append(idx)
        return maxA