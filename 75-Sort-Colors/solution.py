class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        redcount=0
        whilecount=0
        bluecount=0
        
        for num in nums:
            if num==0:
                redcount+=1
            elif num==1:
                whilecount+=1
            else:
                bluecount+=1
        # set the nums
        for i in xrange(redcount):
            nums[i]=0
        for i in xrange(redcount,redcount+whilecount):
            nums[i]=1
        for i in xrange(redcount+whilecount,redcount+whilecount+bluecount):
            nums[i]=2