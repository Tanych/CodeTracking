# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        #print intervals
        i=1
        while i<len(intervals):
           if intervals[i].start>intervals[i-1].end:
               i+=1
               continue
           else:
               # the sorted method aleady done
               #intervals[i-1].start=min(intervals[i-1].start,intervals[i].start)
               intervals[i-1].end=max(intervals[i-1].end,intervals[i].end)
               intervals.pop(i)
        return intervals