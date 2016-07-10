class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left,right=0,n-1
        leftmax=0
        rightmax=0
        total=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]<leftmax:
                    total+=leftmax-height[left]
                else:
                    leftmax=height[left]
                left+=1
            else:
                if height[right]<rightmax:
                    total+=rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
        
        return total
        