class Solution(object):
    def bursthelper(self,memo,nums,left,right):
        if left+1==right: return 0
        if memo[left][right]>0: return memo[left][right]
        res=0
        for i in xrange(left+1,right):
            res=max(res,nums[left]*nums[i]*nums[right]+self.bursthelper(memo,nums,left,i)+\
                self.bursthelper(memo,nums,i,right))
        memo[left][right]=res
        return res
        
    def maxCoinsMemo(self,nums):
        n=len(nums)
        # burst the 0 in middle of nums
        # since the get nothing
        new_nums=[0]*(n+2)
        cnt=1
        for num in nums:
            if num:
                new_nums[cnt]=num
                cnt+=1
        # buidling the new_nums
        new_nums[0]=new_nums[cnt]=1
        cnt+=1
        memo=[[0 for _ in xrange(cnt)] for _ in xrange(cnt)]
        return self.bursthelper(memo,new_nums,0,cnt-1)
    
    def dpmethod(self,nums):
        n=len(nums)
        # burst the 0 in middle of nums
        # since the get nothing
        new_nums=[0]*(n+2)
        cnt=1
        for num in nums:
            if num:
                new_nums[cnt]=num
                cnt+=1
        # buidling the new_nums
        new_nums[0]=new_nums[cnt]=1
        cnt+=1
        dp=[[0 for _ in xrange(cnt)] for _ in xrange(cnt)]
        # k is the diff between left and right
        for k in xrange(2,cnt):
            for left in xrange(0,cnt-k):
                right=left+k
                for i in xrange(left+1,right):
                    dp[left][right]=max(dp[left][right],new_nums[left]*new_nums[i]*new_nums[right]+dp[left][i]+dp[i][right])
        
        return dp[0][cnt-1]
        
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Extend the nums to 1+nums+1
        """
        return self.dpmethod(nums)
        
        n=len(nums)
        new_num=[1]+nums+[1]
        #stote the dpfun values
        dp=[[0 for i in xrange(n+2)] for j in xrange(n+2)]
        
        #get the dpfun
        def dpfun(i,j):
            #if done, return
            if dp[i][j]>0:return dp[i][j]
            #find the max x for depart the i,j,x is the last ele to push out
            #and the final x is for [i-i]*[x]*[j+1]
            #we can simple assume that [2] is the last ele, therefore the nums we can easily understand
            for x in xrange(i,j+1):
                dp[i][j]=max(dp[i][j],dpfun(i,x-1)+new_num[i-1]*new_num[x]*new_num[j+1]+dpfun(x+1,j))
            
            return dp[i][j]
        #return 1-n max value
        return dpfun(1,n)
        