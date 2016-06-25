# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq;
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.interval=[]
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        # since interval can't be sorted, adding tuple for sort
        heapq.heappush(self.interval,(val,Interval(val,val)))
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        res=[]
        while self.interval:
            index,curr_inv=heapq.heappop(self.interval)
            if not res:
                 res.append((index,curr_inv))
            else:
                preindex,pre_inv=res[-1]
                # merge pre and curr,if end+1>=start
                if pre_inv.end+1>=curr_inv.start:
                    pre_inv.end=max(pre_inv.end,curr_inv.end)
                else:
                    res.append((index,curr_inv))
        # update the interval
        self.interval=res
        # get the interval list
        return list(map(lambda x:x[1],res))
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()