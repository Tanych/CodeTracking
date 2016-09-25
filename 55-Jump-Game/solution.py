class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # the same idea is from choose the greatest jump beteew the jump and start
        n=len(nums)
        if n==1:
            return True
            
        #total jump
        tjump=0
        # start choice is 0
        localjump=0
        maxjump=0
        while nums[tjump]>0:
            # directly reacheable return True
            if tjump+nums[tjump]>=n-1:
                return True
            for i in xrange(1,nums[tjump]+1):
                if i+nums[tjump+i]>maxjump:
                    maxjump=i+nums[tjump+i]
                    localjump=i
            # mark the total move step
            tjump+=localjump
            # reset to next iteration
            maxjump=0
            localjump=0
        return False
        