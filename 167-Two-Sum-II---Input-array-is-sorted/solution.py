class Solution(object):
    def binsearch(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
        
    def twosum2(self,nums,target):
        n=len(nums)
        if n<2: return [-1,-1]
        for i in xrange(n):
            if nums[i]<=target:
                idx2=self.binsearch(nums[i+1:],target-nums[i])
                if idx2!=-1:
                    return [i+1,i+1+idx2+1]
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
                
        