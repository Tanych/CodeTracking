class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # try to gernerate all possible value
        # 2^n
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
            res.append(subset)
        return res