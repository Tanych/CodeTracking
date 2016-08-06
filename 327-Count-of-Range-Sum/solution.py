
class FenwickTree(object):
    def __init__(self,n):
        # one dummpy node
        self.bittree=[0]*(n+1)
        self.cnt=n
    
    def lowbit(self, index):

        return index & (-index)
        
    def add(self,index,val):
        if index==0:
            return 
        # it's just add when do update,the val 
        # is the diff from the original value
        while index<=self.cnt:
            self.bittree[index]+=val
            index+=self.lowbit(index)
    
    def getsum(self,index):
        res=0
        while index>0:
            res+=self.bittree[index]
            index-=self.lowbit(index)
        return res    
    
class Solution(object):
    def countrange(self,sums,start,end,upper,lower):
        print sums
        if end-start<=1:return 0
        mid=(start+end)/2
        # do count [start,mid) and [mid,end)
        count=self.countrange(sums,start,mid,upper,lower)+self.countrange(sums,mid,end,upper,lower)
        
        # merge the two half
        k=j=t=mid
        cache=[0]*(end-start)
        s=cache_len=0
        i=start
        while i<mid:
            # found the first pos sums[k]-sums[i]<lower
            while k<end and sums[k]-sums[i]<lower: k+=1
            # found the first pos sums[j]-sums[i]<=upper
            while j<end and sums[j]-sums[i]<=upper: j+=1
            # because the right half is alreay sorted, so
            # we can do as the count
            print j-k
            count+=j-k
            # search the right half to get the smaller
            while t<end and sums[t]<sums[i]:
                cache[s]=sums[t]
                s+=1
                t+=1
            # add the sums[i] to the cache
            cache[s]=sums[i]
            cache_len=s
            s+=1
            i+=1
        # replace the sums with the sored cache
        for i in xrange(cache_len+1):
            sums[start+i]=cache[i]
        return count
        
    def mergesortsolution(self,nums,lower,upper):
        # first get the sum array
        n=len(nums)
        sums=[0]*(n+1)
        for i in xrange(n):
            sums[i+1]=sums[i]+nums[i]
        return self.countrange(sums,0,n+1,lower,upper)
    
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        return self.mergesortsolution(nums,lower,upper)
        """
        we need to number of lower<=prefix_sums[j]-prefix_sums[i-1]<=upper
        In other words, we need to get the number of j between lower+prefix_sums[i-1] and upper+prefix_sums[i-1]
        j > i. and lower + prefix_sums[i] <= prefix_sums[j] <= upper + prefix_sums[i].
    
        1. We need get the value 
        """
        #step 1- prework of sum array
        if not nums:
            return 0
        numLen = len(nums)
        # since if the presum[i]==lower, when we do minus,
        # we wound get 0 if we using lower as the low boundary
        sumArray=[upper,lower-1]
        total=0
        # BuildSortedRanges 
        # 1. add all the possible sum with lower and upper
        for i in xrange(numLen):
            total+=nums[i]
            sumArray+=[total,total+upper,total+lower-1]
        # 2. build a index for the sum array
        index_dict={}
        for index,value in enumerate(sorted(set(sumArray))):
            index_dict[value]=index+1
        
        #use fenwiktree to count the sum
        tree=FenwickTree(len(index_dict))
        res=0
        for i in xrange(numLen-1,-1,-1):
            # add the position of total presum[i] to 1
            tree.add(index_dict[total],1)
            total-=nums[i]
            # count the prenums[i-1]+lower and presums[i-1]+upper
            res+=tree.getsum(index_dict[total+upper])-tree.getsum(index_dict[lower-1+total])
        # finally get the sum of all the possible total value
        return res