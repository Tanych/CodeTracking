# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i=0
        while i<len(intervals):
            if intervals[i].end<newInterval.start:
                i+=1
                continue
            elif intervals[i].start>newInterval.end:
                intervals.insert(i,newInterval)
                return intervals
            else:
                newInterval.start=min(intervals[i].start,newInterval.start)
                newInterval.end=max(intervals[i].end,newInterval.end)
                intervals.pop(i)
        intervals.append(newInterval)
        return intervals
            
                 