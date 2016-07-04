class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[[]]
        for num in nums:
            res+=[i +[num] for i in res if i +[num] not in res]
        return res