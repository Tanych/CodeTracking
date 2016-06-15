class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroindex=-1
        for i in xrange(len(nums)):
            # record the first 0 position
            if zeroindex == -1 and nums[i]==0:
                zeroindex=i
            # swap the data
            if zeroindex!=-1 and nums[i]!=0:
                nums[zeroindex]=nums[i]
                nums[i]=0
                zeroindex+=1
            