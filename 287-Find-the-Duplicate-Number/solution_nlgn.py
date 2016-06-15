class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,middle,right=0,len(nums)/2,len(nums)-1
        while right-left>1:
            # if sum of number less then middle bigger than it should on the smaller part
            if sum(1 for i in nums if i<=middle) >middle:
                right=middle
            else:
                left=middle
            middle=(left+right+1)/2
        return middle