# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #sort the list order by the self.start
        intervals.sort(key=lambda x : x.start)
        
        heap=[]
        for i in xrange(len(intervals)):
            if heap and intervals[i].start>=heap[0]:
                heapq.heapreplace(heap,intervals[i].end)
            else:
                heapq.heappush(heap,intervals[i].end)
        return len(heap)
    
        