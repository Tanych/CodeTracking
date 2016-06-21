class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        set_nums=set()
        for i in xrange(len(nums)):
            if i>k:
                set_nums.remove(nums[i-k-1])
            if True in map(lambda x:abs(x-nums[i])<=t,set_nums):
                return True
            else:
                set_nums.add(nums[i])
        return False