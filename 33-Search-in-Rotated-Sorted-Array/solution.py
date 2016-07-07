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
        
        while left<right:
            mid=left+(right-left)/2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        pivot=right
        
        # search the target compare the real middle nums
        left,right=0,n-1
        while left<=right:
            mid=left+(right-left)/2
            # get the real middle index
            realmid=(pivot+mid)%n
            # find it
            if nums[realmid]==target:
                return realmid
            # if target larger than realmid,
            # it should be on the right part
            # move left to mid
            if nums[realmid]<target:
                left=mid+1
            # if target less than realmid
            # if should be on the left part
            # move to right to mid
            else:
                right=mid-1
                
        return -1