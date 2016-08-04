class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n<3:
            return False
            
        min_num=(1<<31)-1
        max_num=(1<<31)-1
        # first search one ascending pair
        for i in xrange(len(nums)-1):
            if nums[i+1]<=nums[i]:
                continue
            else:
                # if the second has a larger than the preivous two
                if nums[i+1]>max_num or nums[i]>min_num:
                    return True
                # if impossible then restart
                else:
                    min_num=nums[i]
                    max_num=nums[i+1]
                    
        return False