class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        rangexy=lambda x,y:str(x) if x==y else str(x)+'->'+str(y)
        pre,cur,n,res=lower-1,0,len(nums),[]
        for i in xrange(n+1):
            cur=upper+1 if i==n else nums[i]
            if cur-pre>1:
                res.append(rangexy(pre+1,cur-1))
            pre=cur
        return res