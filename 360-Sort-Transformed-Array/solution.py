class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # math problem, a>0 or a<0 is different
        n=len(nums)
        fun=lambda x,a,b,c:a*x*x+b*x+c
        left,right=0,n-1
        res=[0]*n
        idx=n-1 if a>=0 else 0
        while left<=right:
            # up
            if a>=0:
                if fun(nums[right],a,b,c)>fun(nums[left],a,b,c):
                    res[idx]=fun(nums[right],a,b,c)
                    right-=1
                else:
                    res[idx]=fun(nums[left],a,b,c)
                    left+=1
                idx-=1
            #down
            else:
                if fun(nums[right],a,b,c)>fun(nums[left],a,b,c):
                    res[idx]=fun(nums[left],a,b,c)
                    left+=1
                else:
                    res[idx]=fun(nums[right],a,b,c)
                    right-=1
                idx+=1
        return res