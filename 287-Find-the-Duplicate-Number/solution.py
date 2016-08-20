class Solution(object):
    def usingcycle(self, nums):
        """
        building index to number relationship
        EX: 2 1 3 1
        0->2 1->1 2->3 1->1 
        according to the index building the route
        0->2->3->1->1  the cycle start point is the duplicate
        """
        slow=nums[0]
        fast=nums[nums[0]]
        
        while fast!=slow:
            slow=nums[slow]
            fast=nums[nums[fast]]
        # go to equal len from head
        fast=0
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]
        return fast
        
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.usingcycle(nums)
        
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)/2
            cnt=0
            # cnt the number less than or equal n/2
            # using the drawer 
            for num in nums:
                if num<=mid:
                    cnt+=1
            # if the cnt larger than mid, it should be 
            # on the left and the drawer should be less
            if cnt>mid:
                right=mid-1
            else:
                left=mid+1
        return left