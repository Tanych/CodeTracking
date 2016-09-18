class Solution(object):
    def helper(self,num,k,res):
        if k==0:
            res.append(str(num))
            return
        n=len(num)
        if k>=n:
            return
        # find the min index
        minidx=0
        for i in xrange(1,k+1):
            if num[i]<num[minidx]:
                minidx=i
        res.append(num[minidx])
        self.helper(num[minidx+1:],k-minidx,res)
        
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # main idea is to find the min index in k substring
        res=[]
        self.helper(num,k,res)
        return str(int(''.join(res))) if res else '0'