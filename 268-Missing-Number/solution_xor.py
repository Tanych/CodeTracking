class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum xor is the common way to deal with the missing
        missing = i = 0
        # xor the number in nums
        while i < len(nums):
            missing ^= i ^ nums[i]
            i+=1
        # xor the n
        return missing ^ i