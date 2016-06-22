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
        if n<2 or k<1 or t<0:
            return False
        buckets={}
        width=t+1
        for i in xrange(n):
            id=self.getBucketID(nums[i],width)
            if id in buckets:
                return True
            if (id-1 in buckets and abs(nums[i]-buckets[id-1]<width)) or \
                    (id+1 in buckets and abs(buckets[id+1]-nums[i]<width)):
                return True
            buckets[id] = nums[i]
            if i>=k:
                del buckets[self.getBucketID(nums[i - k], width)]
        return False