class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res=[0]*(length+1)
        
        for update in updates:
            res[update[0]]+=update[2]
            # the pos behind the end should minus the update
            res[update[1]+1]-=update[2]
        
        for i in xrange(1,len(res)):
            res[i]+=res[i-1]
        return res[:-1]
        