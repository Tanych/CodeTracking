class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp=rp=1
        max_product=nums[0]
        n=len(nums)
        for i in xrange(n):
            lp*=nums[i]
            rp*=nums[n-1-i]
            max_product=max(max_product,max(lp,rp))
            # reset
            if lp==0:
                lp=1
            if rp==0:
                rp=1
        return max_product