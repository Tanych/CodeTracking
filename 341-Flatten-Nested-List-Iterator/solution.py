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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack=[]
        self.hashmaping={}
        self.maxdepth=0
        # reverse the order, when we pop we get the first
        for i in xrange(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[i])
        
        unweight=weighted=0
        while len(nestedList):
            nextlevel=[]
            for li in nestedList:
                if li.isInteger():
                    unweight+=li.getInteger()
                else:
                    nextlevel.extend(li.getList())
            weighted+=unweight
            nestedList=nextlevel
        #print weighted
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top=self.stack[-1]
            # if it's interge, directly return true
            if top.isInteger():
                return True
            # if it's a list, put all the element in list to the stack
            # first get it out
            self.stack.pop()
            # then add them singlely
            for i in xrange(len(top.getList())-1,-1,-1):
                self.stack.append(top.getList()[i])
        
        return False
            
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())