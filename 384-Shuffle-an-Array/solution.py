class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums=nums
        self.setnum=[]
        
        def dfs(nums,path):
            if len(path)==len(self.nums):
                self.setnum.append(path)
                return
            for i in xrange(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
    
        for i in xrange(len(self.nums)):
            dfs(self.nums[:i]+self.nums[i+1:],[self.nums[i]])
        
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

        return self.setnum[random.randint(0,len(self.setnum)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()