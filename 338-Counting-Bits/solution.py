class Solution(object):
    def countone(self,s):
        count=0
        for ch in s:
            if ch=='1':
                count+=1
        return count
        
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[]
        for i in xrange(num+1):
            res.append(self.countone(bin(i)[2:]))
        return res