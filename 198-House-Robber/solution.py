class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n=len(nums)
        
        dp=[0 for _ in xrange(n+1)]
        
        
        for i in xrange(1,n+1):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
            
        return max(dp)
        