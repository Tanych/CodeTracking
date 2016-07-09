class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # using the maxstep to record the max step before i can reach
        # if i reach the maxstep but can't move on then return False
        n=len(nums)
        maxstep=0
        
        for i in xrange(n):
            # if i reach the maxstep, that means it can't move on 
            if i>maxstep:
                return False
            # record the max step that can jump
            maxstep=max(maxstep,i+nums[i])
        return True