class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        if numRows==0:
            return res
        if numRows==1:
            return [[1]]
        res=[[1]]
        for i in xrange(1,numRows):
            nextList=[1]
            for j in xrange(1,len(res[i-1])):
                nextList.append(res[i-1][j]+res[i-1][j-1])
            nextList.append(1)
            res.append(nextList)
        return res