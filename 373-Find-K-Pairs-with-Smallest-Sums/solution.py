class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
     
        heapsum=[]
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(heapsum,(n1+n2,n1,n2))
        res=[]
        if heapsum:
            # k might out of boundary
            for i in xrange(min(k,len(nums1)*len(nums2))):
                _,n1,n2=heapq.heappop(heapsum)
                res.append([n1,n2])
        return res