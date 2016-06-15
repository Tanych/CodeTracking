class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        while i<len(nums):
            if nums[i]==0:
                j=i+1
                while j<len(nums):
                    if nums[j]!=0:
                        # swap
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                    j+=1
            i+=1
            