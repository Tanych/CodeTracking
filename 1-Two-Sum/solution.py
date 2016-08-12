class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i,num in enumerate(nums):
            if num not in check:
                check[target-num]=i
            else:
                return [min(i,check[num]),max(i,check[num])]
        