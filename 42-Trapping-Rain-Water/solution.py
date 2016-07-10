class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #n=len(height)
        total=0
        for i in xrange(1,len(height)-1):
            leftmax=max(height[:i])
            rightmax=max(height[i+1:])
            if leftmax<=height[i] or rightmax<=height[i]:
                continue
            total+=min(leftmax,rightmax)-height[i]
        
        return total
        