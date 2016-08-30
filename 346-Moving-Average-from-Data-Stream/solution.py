class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq=collections.deque([])
        self.size=size
        self.sumval=0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.dq)<self.size:
            self.sumval+=val
            self.dq.append(val)
            return float(self.sumval)/float(len(self.dq))
        else:
            v=self.dq.popleft()
            self.sumval-=v
            self.sumval+=val
            self.dq.append(val)
            return float(self.sumval)/float(self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)