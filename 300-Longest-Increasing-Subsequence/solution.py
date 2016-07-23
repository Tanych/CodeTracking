class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        first method is DP:
        define: dp[i] means the s[0:i] LIS
        initial: dp[i]=1 since including themselves
        general:
        for j before i, if nums[i]>nums[j], res=max(dp[i],dp[j]+1)
        """
        n=len(nums)
        if not nums or n==1:
            return n
        
        dp=[1]*n
        
        for i in xrange(1,n):
            for j in xrange(i):
                # update the max depend on dp previous
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        # get the maxium
        return max(dp)
            
        
                
            