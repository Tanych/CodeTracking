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
        #queue=collections.deque()
        #for num in nums:
        #    queue.append(num)
        res=[]
        i=0
        while i<=n-k:
            res.append(max(nums[i:k+i]))
            #queue.popleft()
            i+=1
        return res