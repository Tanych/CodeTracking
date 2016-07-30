class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k==0:
            return []
        n=len(nums)
        queue=collections.deque()
        res=[]
        """
        using the deque to store the idx of the value
        every time pop out the index out of range
        """
        for i in xrange(n):
            # pop ele out of range
            while queue and queue[0]<i-k+1:
                queue.popleft()
            # discard the num that smaller than the new comer
            # since it's on the left, it's impossible for them
            # to be the candicate for the next windows
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
                
            queue.append(i)
            
            # get the result, it's the first num in the deque
            if i>=k-1:
                res.append(nums[queue[0]])
                
        return res
        