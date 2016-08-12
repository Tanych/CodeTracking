class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums=nums
        self.shuff=[num for num in nums]
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if not self.nums:
            return []
        n=len(self.shuff)
        for i in xrange(n-1,-1,-1):
            idx=random.randint(0,n-1)
            self.shuff[idx],self.shuff[i]=self.shuff[i],self.shuff[idx]
            
        return self.shuff


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()