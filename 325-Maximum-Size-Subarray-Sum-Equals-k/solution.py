class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        mapping={0:0}
        n=len(nums)
        sumnum=0
        res=-1<<31
        for i in xrange(1,n+1):
            sumnum+=nums[i-1]
            target=sumnum-k
            if target in mapping:
                res=max(res,i-mapping[target])
            if sumnum not in mapping:
                mapping[sumnum]=i
        return 0 if res==-1<<31 else res