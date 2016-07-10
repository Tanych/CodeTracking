class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n<=2:
            return 0
        # using two pointer calc the total above area
        left,right=0,n-1
        # record the min height
        minh=0
        #above area total
        tarea=0
        while left<right:
            # if equal to the min, move on
            if height[left]<=minh:
                left+=1
            elif height[right]<=minh:
                right-=1
            elif height[right]>=height[left]:
                # the relative height
                tarea+=(right-left+1)*(height[left]-minh)
                minh=height[left]
                left+=1
            elif height[right]<height[left]:
                # the relative height
                tarea+=(right-left+1)*(height[right]-minh)
                minh=height[right]
                right-=1
        # deal with the end
        # if the the last height is larger than the min height
        # then return the diff of the height
        if height[right]-minh>0:
            tarea+=(height[right]-minh)
        # the trap volume is the total above area minus the total height
        # the height is solid
        return tarea-sum(height)