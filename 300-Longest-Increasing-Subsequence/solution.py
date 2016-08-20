class Solution(object):
    def lengthOfLISBIS(self,nums):
        """
        the bin search method is trying to 
        """
        n=len(nums)
        if not nums or n==1:
            return n
        res=[nums[0]]
        
        for i in xrange(1,n):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                # try to find the value more closer to nums[i]
                #pos=bisect.bisect_left(res, nums[i])
                left,right=0,len(res)
                while left<right:
                    mid=(left+right)/2
                    if res[mid]==nums[i]:
                        left=mid
                        break
                    if res[mid]>nums[i]:
                        right=mid
                    else:
                        left=mid+1
                res[left]=nums[i]
                
        return len(res)
    
    def binsearch(self,nums,left,right,target):
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
        
    def lengthOfLIS3(self, nums):
        """
        using patience sort to find the subsequence
        """
        n=len(nums)
        if not n:
            return 0
        
        # record the tails
        nlen=0
        tails=[0]*n
        tails[0]=nums[0]
        
        for i in xrange(1,n):
            # s1 less than smallest
            if nums[i]<tails[0]:
                tails[0]=nums[i]
            # s2 larger than lagest
            elif nums[i]>tails[nlen]:
                nlen+=1
                tails[nlen]=nums[i]
            # in the mid
            else:
                tails[self.binsearch(tails,0,nlen,nums[i])]=nums[i]
        #print tails[:nlen+1]
        return nlen+1
        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        first method is DP:
        define: dp[i] means the s[0:i] LIS
        initial: dp[i]=1 since including themselves
        general:
        for j before i, if nums[i]>nums[j], res=max(dp[i],dp[j]+1)
        """
        return self.lengthOfLIS3(nums)
        
        n=len(nums)
        if not nums or n==1:
            return n
        
        dp=[1]*n
        
        for i in xrange(1,n):
            for j in xrange(i):
                # update the max depend on dp previous
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        # get the maxium
        return max(dp)
            
        
                
            