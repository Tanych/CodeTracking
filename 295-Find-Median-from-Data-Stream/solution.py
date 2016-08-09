from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #the small part with max heap (invert with negative)
        self.small=[]
        #the large part with min heap
        self.large=[]
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small)==len(self.large):
            heappush(self.large,-heappushpop(self.small,-num))
        else:
            heappush(self.small,-heappushpop(self.large,num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small)==len(self.large):
            return (self.large[0]-self.small[0])/2.0
        else:
            return 1.0*self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()