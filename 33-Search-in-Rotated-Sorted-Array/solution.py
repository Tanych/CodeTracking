class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # step1-- first find the pivot of the rotated array
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            # deal with the two elements[2,1]
            if right-left==1:
                if nums[right]==target:
                    return right
                elif nums[left]==target:
                    return left
                    
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1

        return -1