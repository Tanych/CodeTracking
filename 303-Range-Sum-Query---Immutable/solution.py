class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n=len(nums)
        self.dp=[0 for _ in xrange(n+1)]
        
        for i in xrange(1,n+1):
            self.dp[i]=self.dp[i-1]+nums[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return  self.dp[j+1]-self.dp[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)