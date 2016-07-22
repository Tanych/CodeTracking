class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n=len(s)
        if n<=numRows:
            return s
        
        resstable=[[] for _ in xrange(numRows)]
        i=0
        while i<n:
            idx=0
            while i<n and idx<numRows:
                resstable[idx].append(s[i])
                idx+=1
                i+=1
            idx=numRows-2
            while idx>=1 and i<n:
                resstable[idx].append(s[i])
                idx-=1
                i+=1
        res=''
        for i in xrange(len(resstable)):
            res+=''.join(resstable[i])
        return res
        