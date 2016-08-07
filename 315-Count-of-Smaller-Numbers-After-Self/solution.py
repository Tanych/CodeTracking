class FenwikenTree(object):
    def __init__(self,n):
        self.sumarray=[0]*(n+1)
        self.n=n
    
    def lowbit(self,x):
        return x & (-x)
    
    def add(self,x,val):
        if x==0: return
        while x<=self.n:
            self.sumarray[x]+=val
            x+=self.lowbit(x)
    
    def sum(self,x):
        res=0
        while x>0:
            res+=self.sumarray[x]
            x-=self.lowbit(x)
        return res
            
class Solution(object):
    def binsearch(self,nums):
        n=len(nums)
        tmp=[]
        res=[0]*n
        for i in xrange(n-1,-1,-1):
            left,right=0,len(tmp)
            while left<right:
                mid=(left+right)/2
                # if equal we don't count as 1 it's 0
                if tmp[mid]>=nums[i]:
                    right=mid
                else:
                    left=mid+1
            res[i]=right
            tmp.insert(right,nums[i])
        return res
        
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.binsearch(nums)
        
        index_dict={}
        for index,value in enumerate(sorted(nums)):
            index_dict[value]=index+1
        
        tree=FenwikenTree(len(nums))
        
        res=[0]*len(nums)
        #print index_dict
        for i in xrange(len(nums)-1,-1,-1):
            tree.add(index_dict[nums[i]],1)
            res[i]=tree.sum(index_dict[nums[i]]-1)
        return res
        
        