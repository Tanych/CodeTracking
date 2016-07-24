class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n=len(nums)
        
        if n<4:
            return max(nums)
            
        dpnofirst=[0 for _ in xrange(n+1)]
        dpnolast=[0 for _ in xrange(n+1)]
        
        for i in xrange(2,n+1):
            dpnofirst[i]=max(dpnofirst[i-1],nums[i-1]+dpnofirst[i-2])
        
        for i in xrange(1,n):
            dpnolast[i]=max(dpnolast[i-1],nums[i-1]+dpnolast[i-2])
            
        return max(max(dpnofirst),max(dpnolast))
        