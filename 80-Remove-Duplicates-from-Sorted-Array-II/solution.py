class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        i=1
        count=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                if count==2:
                    nums.pop(i)
                else:
                    count+=1
                    i+=1
            else:
                i+=1
                count=1
        return len(nums)