class Solution(object):
    def findPeakElement2(self,nums):
        """
        find the number of peak ele in an array
        """
        cnt=t=0
        for i in xrange(1,len(nums)):
           if nums[i-1]==nums[i]:
               continue
           if not t:
               t=1 if nums[i-1]<nums[i] else -1
               continue
           if (nums[i]>nums[i-1] and t==-1) or\
                (nums[i]<nums[i-1] and t==1):
                  cnt+=1
                  t=1 if t==-1 else -1
        return 1 if t==0 else cnt
            
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return self.findPeakElement2(nums)
        left,right=0,len(nums)-1
        while left<right:
            if nums[left+1]>nums[left]:
                left+=1
            else:
                return left
            if nums[right-1]>nums[right]:
                right-=1
            else:
                return right
        return right
            
        