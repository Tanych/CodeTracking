class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # first lets do in naive way
        
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            mid=(right+left)/2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]:
                left+=1
            elif nums[mid]>nums[left]:
                # if every num in nums[left:mid] bigger than target or smaller than target
                if nums[mid]<=target or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                # if every num in nums[mid:right] bigger than target or smaller than target
                if nums[right]<target or target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return False
                    