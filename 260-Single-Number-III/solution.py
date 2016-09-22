class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        num_len=len(nums)
        if num_len<=2:
            return nums
        # get b^c
        bandc=0
        for i in xrange(num_len):
            bandc^=nums[i]
        #xor = b^c， to get the b or c
        # get the first different pos in bc
        bit_pos=0
        for i in xrange(32):
            if (bandc>>i)&1:
                bit_pos=i
                break
        # xor (b or c )and other num
        borc=0
        for i in xrange(num_len):
            if (nums[i]>>bit_pos)&1:
                borc^=nums[i]
        # get b or c
        res.append(borc)
        # get another number
        res.append(bandc^borc)
        return res
        