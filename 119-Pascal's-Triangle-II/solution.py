class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        if rowIndex==0:
            return [1]
        res=[1]
        for i in xrange(1,rowIndex+1):
            nextList=[1]
            for j in xrange(1,len(res)):
                nextList.append(res[j]+res[j-1])
            nextList.append(1)
            res=nextList
        return res