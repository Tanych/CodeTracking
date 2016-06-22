class Solution(object):
    def getBucketID(self, i, w):
        return (i + 1) / w - 1 if i<0 else i/w
        
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n=len(nums)
        # kick out the special
        if n<2 or k<1 or t<0:
            return False
        # the buckets has a width with t+1, the nums[i], nums[j] has two situation
        # p1: in the same bucket, p2: in the neighor bucket
        buckets={}
        width=t+1
        for i in xrange(n):
            id=self.getBucketID(nums[i],width)
            # nums[i], nums[j] in the same buckets
            if id in buckets:
                return True
            # nums[i], nums[j] in the neighor buckets
            if (id-1 in buckets and nums[i]-buckets[id-1]<width) or \
                    (id+1 in buckets and buckets[id+1]-nums[i]<width):
                return True
            buckets[id] = nums[i]
            # if |i-j|>k, then kick out the k before element
            if i>=k:
                del buckets[self.getBucketID(nums[i - k], width)]
        return False