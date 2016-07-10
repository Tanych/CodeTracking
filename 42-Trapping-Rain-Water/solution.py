class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left,right=0,n-1
        # using to max to set the wall of each side
        leftmax=0
        rightmax=0
        total=0
        while left<=right:
            # if the right wall is eough higher
            if height[left]<=height[right]:
                # count the left part of the sunk down
                if height[left]<leftmax:
                    total+=leftmax-height[left]
                else:
                    # the count a new higher wall, update
                    leftmax=height[left]
                left+=1
            else:
                # the same with left part
                if height[right]<rightmax:
                    total+=rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
        
        return total
        