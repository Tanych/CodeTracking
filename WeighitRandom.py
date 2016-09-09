import random
class WRandom(object):
    def __init__(self,nums):
        self.nums=nums
        self.prob=[0 for _ in xrange(len(nums))]
        self.prob[0]=nums[0]
        for i in xrange(1,len(nums)):
            self.prob[i]=self.prob[i-1]+nums[i]
    def binsearch(self,target):
        left,right=0,len(self.prob)-1
        while left<=right:
            mid=(left+right)/2
            if self.prob[mid]==target:
                return mid
            elif self.prob[mid]>target:
                right=mid-1
            elif self.prob[mid]<target:
                left=mid+1
        return right+1
    
    def nextint(self):
        target=random.randint(0,len(self.prob))
        print target
        return self.nums[self.binsearch(12)]
nums=[1,4,2,6]
t=WRandom(nums)
print t.nextint()
