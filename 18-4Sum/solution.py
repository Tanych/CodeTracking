class Solution(object):
    def nsum(self,nums,start,n,target):
        nlen=len(nums)
        res=[]
        if nums[start]*n>target or target>nums[nlen-1]*n:
            return res
        
        for i in xrange(start,nlen-n+1):
            if i>start and nums[i-1]==nums[i]:
                continue
            if n==1:
                if target<nums[i]:break
                if target>nums[i]:continue
                res.append([target])
                break
            for li in self.nsum(nums,i+1,n-1,target-nums[i]):
                li.append(nums[i])
                res.append(li)
        return res
        
    def fourSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        num_len=len(nums)
        
        if num_len<4:
            return []

        nums.sort()
        
        return self.nsum(nums,0,4,target)
        
        
        res_list=[]
        hash_dict={}

        for m in xrange(num_len-3):
            if 4*nums[m]>target:
                return res_list
            for i in xrange(m+1,num_len-2):
                start=i+1
                end=num_len-1
                while start<end:
                    if nums[m]+nums[i]+nums[start]+nums[end]==target:
                        if not hash_dict.has_key((nums[m],nums[i],nums[start],nums[end])):
                            res_list.append([nums[m],nums[i],nums[start],nums[end]])
                            hash_dict[(nums[m],nums[i],nums[start],nums[end])]=1
                        start+=1
                        end-=1
                    elif nums[m]+nums[i]+nums[start]+nums[end]<target:
                        start+=1
                    elif nums[m]+nums[i]+nums[start]+nums[end]>target:
                        end-=1

        return res_list
        