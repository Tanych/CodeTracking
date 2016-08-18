class Solution(object):
    def twosum2(self,nums,target):
        n=len(nums)
        if n<2: return [-1,-1]
        left,right=0,n-1
        while left<right:
            sum_nums=nums[left]+nums[right]
            if sum_nums==target:
                return [left+1,right+1]
            elif sum_nums<target:
                left+=1
            else:
                right-=1
        return [-1,-1]
        
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.twosum2(numbers,target)
        n=len(numbers)
        if n<2: return [-1,-1]
        hashmap={}
        for i in xrange(n):
            if numbers[i] in hashmap:
               return [hashmap[numbers[i]],i+1]
               
            if numbers[i]<=target:
                hashmap[target-numbers[i]]=i+1
        return [-1,-1]
                
        