class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        n=len(nums)
        for i in xrange(2**n):
            subset=[]
            # using the binary move
            bn=bin(i)[2:]
            # 001, make all the same length
            bn='0'*(n-len(bn))+bn
            for j in xrange(len(bn)):
                if bn[j]=='1':
                    subset.append(nums[j])
            if subset not in res:
                res.append(subset)
        return res