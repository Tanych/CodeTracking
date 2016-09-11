class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums=nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([idx for idx,num in enumerate(self.nums) if num==target])
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)