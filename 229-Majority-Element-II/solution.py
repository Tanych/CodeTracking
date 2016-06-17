class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        return map(lambda v:v[0], filter(lambda v:v[1]>len(nums)/3, Counter(nums).items()))