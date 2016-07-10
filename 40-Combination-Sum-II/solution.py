class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def recurhelper(nums,res,path,target,start):
            if target==0:
                res.append(path)
                return
            if target<0:
                return
            for i in xrange(start,len(nums)):
                # ignore the duplicate start from i
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # reduce count
                if nums[i]>target:
                    break
                if nums[i]<=target:
                    recurhelper(nums[:i]+nums[i+1:],res,path+[nums[i]],target-nums[i],i)


        res=[]
        candidates.sort()
        recurhelper(candidates,res,[],target,0)
        return res