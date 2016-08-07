class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1_len=len(nums1)
        num2_len=len(nums2)
        
        if k>(num1_len+num2_len):
            return -1
            
        ret=[0]*k
        
        for i in xrange(0,k+1):
            j=k-i
            if i>num1_len or j>num2_len:
                continue
            left=self.maxsubstringNum(nums1,i)
            right=self.maxsubstringNum(nums2,k-i)
            num=self.merge(left,right)
            #print num
            ret=max(num,ret)
        return ret
    
    def merge(self,left,right):
        """
        :type left: List[int], the left part of maxinum
        :type right: List[int], the right part of the maxinum
        :rtype: List[int], the maxinum value using the two parts
        """
        res=[]
        #print left,right
        while left or right:
            if left>right:
                res.append(left[0])
                left=left[1:]
                
            else:
                res.append(right[0])
                right=right[1:]
        return res
        
    
    def maxsubstringNum(self,nums,k):
        """
        :type nums: List[int], the number list select from
        :type k: int, the number of numbers need selected
        :rtype: List[int], the max selcts sequence in nums
        """
        #store the max vaule position
        max_poslist=[-1]
        num_len=len(nums)
        if k > num_len : return max_poslist
        res=[-1]*k
        plen=0
        for i in xrange(num_len):
            # plen is the result length and num_len-i is the left length
            # we need keep that the left should be large than k-plen
            # if the previous is smaller we replaced it the bigger
            while plen>0 and plen+(num_len-i)>k and res[plen-1]<nums[i]:
                plen-=1
            if plen<k:
                res[plen]=nums[i]
                plen+=1
        return res
        
        