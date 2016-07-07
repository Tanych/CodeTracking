class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # first lets do in naive way
        
        if target in nums:
            return True
        else:
            return False