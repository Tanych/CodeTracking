class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the same idea is from choose the greatest jump beteew the jump and start
        n=len(nums)
            
        #total pos
        step=0
        nxstep=0
        i=0
        while i<n-1:
            step+=1
            nxstep+=1
            maxstep=0
            # directly reacheable return True
            if i+nums[i]>=n-1:
                break
            for j in xrange(1,nums[i]+1):
                if j+nums[i+j]>maxstep:
                    maxstep=j+nums[i+j]
                    nxstep=j+i
            # mark the total move step
            i=nxstep
          
        return step
        