
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #first sort the array
    
        n=len(nums)
        for i in xrange(n-1):
            if not i%2 and nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            if i%2 and nums[i]<nums[i+1]:
                 nums[i],nums[i+1]=nums[i+1],nums[i]
        