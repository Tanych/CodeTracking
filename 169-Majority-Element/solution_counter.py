class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # high performance of counter
        from collections import Counter
        cntdict = Counter(nums).items()                          
        eletuple = (k for (k,v) in cntdict if v > len(nums) / 2) 
        return next(eletuple)