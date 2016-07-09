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
            
        #total pos
        tpos=0
        # start choice is 0
        kpos=0
        maxstep=0
        while nums[tpos]>0:
            # directly reacheable return True
            if tpos+nums[tpos]>=n-1:
                return True
            for i in xrange(1,nums[tpos]+1):
                if i+nums[tpos+i]>maxstep:
                    maxstep=i+nums[tpos+i]
                    kpos=i
            # mark the total move step
            tpos+=kpos
            # reset to next iteration
            maxstep=0
            kpos=0
        return False
        