class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        count=1
        start=nums[0]                    
        for i in xrange(1,n):
            if nums[i]!=start:
                count-=1
            else:
                count+=1
            # update the value
            if count==0:
                start=nums[i]
                count=1
        return start
                