class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.res=[]
        if v1:
            self.res.append(v1)
        if v2:
            self.res.append(v2)
    def next(self):
        """
        :rtype: int
        """
        tmp=self.res.pop(0)
        ret=tmp.pop(0)
        if tmp:
            self.res.append(tmp)
        return ret
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.res)!=0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())