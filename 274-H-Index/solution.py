class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n=len(citations)
        # record the number of paper has cited i times
        # [3,0,1,5,6]
        # [1,1,0,1,0,2]
        
        stats=[0]*(n+1)
        for i in xrange(n):
            if citations[i]>=n:
                stats[n]+=1
            else:
                stats[citations[i]]+=1
        snum=0
        # search the hindex
        for i in xrange(n,-1,-1):
            snum+=stats[i]
            # if the number of paper whihc cited more than i time larger or equal than
            # i, that's the H-index
            if snum>=i:
                return i
        return 0
            