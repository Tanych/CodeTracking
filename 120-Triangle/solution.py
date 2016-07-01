class Solution(object):
    def dfshelper(self,nums,level,pos):
        # recur stop
        if level==len(nums)-1:
            return [[nums[level][pos]]]
        else:
            # path left
            lp=[[nums[level][pos]]+ch for ch in self.dfshelper(nums,level+1,pos)]
            # right path
            rp=[[nums[level][pos]]+ch for ch in self.dfshelper(nums,level+1,pos+1)]
            return lp+rp
            
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return min(sum(li) for li in self.dfshelper(triangle,0,0))