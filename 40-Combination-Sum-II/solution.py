class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def recurhelper(nums,res,path,target,start):
            if target==0:
                if path not in res:
                    res.append(path)
                return
            if target<0:
                return
            if target>0:
                for i in xrange(start,len(nums)):
                    if nums[i]<=target:
                        recurhelper(nums[:i]+nums[i+1:],res,path+[nums[i]],target-nums[i],i)


        res=[]
        candidates.sort()
        recurhelper(candidates,res,[],target,0)
        return res