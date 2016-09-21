class binIndexTree(object):
    def __init__(self,n):
        self.nums=[0]*n
        self.sumarr=[0]*(n+1)
        self.maxlen=n
    def lowbit(self,x):
        return x&(-x)
    def update(self,x,val):
        diff=val-self.nums[x]
        self.nums[x]=val
        x+=1
        while x<=self.maxlen:
            self.sumarr[x]+=diff
            x+=self.lowbit(x)
    def sumarray(self,x):
        x+=1
        res=0
        while x>0:
            res+=self.sumarr[x]
            x-=self.lowbit(x)
        return res
                 
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.btree=binIndexTree(len(nums))
        for i,num in enumerate(nums):
            self.btree.update(i,num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.btree.update(i,val)
        
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.btree.sumarray(j)-self.btree.sumarray(i-1)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)