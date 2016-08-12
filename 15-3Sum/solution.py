class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        
        if n<3:
            return []

        nums.sort()
        res=[]
        i=0
        while i<n-2:
            if nums[i]>0:break
            start,end=i+1,n-1
            while start<end:
                sum_num=nums[i]+nums[start]+nums[end]
                if sum_num==0: 
                    res.append([nums[i],nums[start],nums[end]])
                if sum_num>=0:
                    # skip the duplicate num
                    preend=end
                    end-=1
                    while nums[end]==nums[preend] and start<end:
                        preend=end
                        end-=1
                if sum_num<=0:
                    prestart=start
                    start+=1
                    while nums[prestart]==nums[start] and start<end:
                        prestart=start
                        start+=1
            # skip the duplicate result [-1,-1,-1,0,2]
            prei=i
            i+=1
            while nums[prei]==nums[i] and i<n-2:
                prei=i
                i+=1

        return res
        
                