class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # set window size for the set
        set_nums=set()
        for i in xrange(len(nums)):
            if i>k:
                set_nums.remove(nums[i-k-1])
            if nums[i] in set_nums:
                print nums[i]
                return True
            else:
                set_nums.add(nums[i])
        return False