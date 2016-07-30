class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        greedy=[1 for _ in xrange(n)]
        
        for i in xrange(1,n):
            if ratings[i]>ratings[i-1]:
                greedy[i]=greedy[i-1]+1
        
        for i in xrange(n-1,0,-1):
            if ratings[i-1]>ratings[i]:
                greedy[i-1]=max(greedy[i]+1,greedy[i-1])
        
        return sum(greedy)
        