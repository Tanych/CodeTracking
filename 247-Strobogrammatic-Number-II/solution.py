class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=self.recurhelper(n)
        if n!=1:
            #exculde the first element in 0
            return [a for a in res if a[0] !='0'] 
        else:
            return res
            
    def recurhelper(self,n):
        if n==0: 
            return ['']
        if n == 1: 
            return ['0','1','8']
        if n==2: 
            return ['00','11','69','88','96']
        res=[]
        for ele in ['00','11','69','88','96']:
            curr=[]
            for ch in self.recurhelper(n-2):
                curr.append(ele[0]+ch+ele[1])
            res+=curr
        return res
                        