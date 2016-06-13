class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        for i in xrange(len(height)):
            for j in xrange(i+1,len(height)):
                maxarea = (j-i)*(height[i]+height[j])/2
                if maxarea >max:
                    max = maxarea
        return max