class Solution(object):
    def dfs(self,stones,graph,curpos,lastjump):
        if curpos==stones[-1]:
            return True
        # since the jump need based on lastjump
        # only forward,get rid of the stay at the same pos
        rstart=max(curpos+lastjump-1,curpos+1)
        rend=min(curpos+lastjump+1,stones[-1])+1
        for nextpos in xrange(rstart,rend):
            if nextpos in graph and self.dfs(stones,graph,nextpos,nextpos-curpos):
                return True
        return False
    
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return True
        if stones[1]!=1:
            return False
        graph={val:idx for idx,val in enumerate(stones)}
        return self.dfs(stones,graph,1,1)
        