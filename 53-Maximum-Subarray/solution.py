class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # to make the sum as most as bigger, 
        # we need to find i,j to make cursum[i]-cursum[j] as close to inf
        n=len(nums)
        maxsum=cursum=nums[0]
        for i in xrange(1,n):
            # if cursum[i-1] less than 0,no need to carry to current
            # make it recounter
            cursum=max(nums[i], cursum+nums[i])
            # check the maxsum
            maxsum=max(cursum,maxsum)
        return maxsum