# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s: return NestedInteger()
        if s[0]!='[': return NestedInteger(int(s))
        
        i,stck=0,[]
        for j in xrange(len(s)):
            if s[j]=='[':
                stck.append(NestedInteger())
                i=j+1
            elif s[j]==']':
                # add single int
                if s[j-1].isdigit():
                    stck[-1].add(NestedInteger(int(s[i:j])))
                # add to the level of nest
                if len(stck)>1:
                    cur=stck.pop()
                    stck[-1].add(cur)
            # add singel int to the nestint
            elif s[j]==',':
                if s[j-1].isdigit():
                    stck[-1].add(NestedInteger(int(s[i:j])))
                # avoid [-1,-2] single int no other nest
                i=j+1
        return stck[-1]
   
            