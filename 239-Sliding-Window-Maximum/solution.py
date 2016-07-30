class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k==0:
            return []
        queue=collections.deque()
        for num in nums:
            queue.append(num)
        res=[]
        print queue[0]
        while k<=len(queue):
            res.append(max([queue[i] for i in xrange(k)]))
            queue.popleft()
        return res