class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num[i] should be in the pos num[i]-1
        # swap the value in the nums,
        # find the first value that not math the position
        n=len(nums)
        for i in xrange(n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        
        # check the array
        for i in xrange(n):
            if nums[i]!=i+1:
                return i+1
        # reach the bounary
        return n+1
                    
        