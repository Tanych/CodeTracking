class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,num,start,path):
        if num==1:
            if len(path)>1:
                self.res.append(path)
            return
        for i in xrange(start,num+1):
            if num%i==0:
                self.helper(num/i,i,path+[i])
        
            
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.helper(n,2,[])
        return self.res
        