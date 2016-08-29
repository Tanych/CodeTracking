# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def __init__(self):
        self.mapping={}
    
    def dfs(self,nestedList,level):
        for ele in nestedList:
            if ele.isInteger():
                self.mapping[level]=self.mapping.get(level,0)+ele.getInteger()
            else:
                self.dfs(ele.getList(),level+1)
                
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.dfs(nestedList,1)
        res=0
        for k in self.mapping:
            res+=self.mapping[k]*k
        return res
        