class Solution(object):
    def helper(self,n):
        if n==0:
            return ['0']
        if n==1:
            return ['0','1']
        res=[]
        pre=self.helper(n-1)
        for num in pre:
            res.append(chr(48)+num)
        
        for num in pre[::-1]:
            res.append(chr(48+1)+num)
        return res
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        res=self.helper(n)
        return [int(x,2) for x in res]