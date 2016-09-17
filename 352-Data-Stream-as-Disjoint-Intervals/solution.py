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
        self._data=[]
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self._data:
            self._data.append(Interval(val,val))
            return 
        
        self._data.sort(cmp=lambda x,y:x.start-y.start)
 
        # search lower bound
        nlen=len(self._data)
        left,right=0,nlen
        while left<right:
            mid=(left+right)/2
            if self._data[mid].start>=val:
                right=mid
            else:
                left=mid+1
                
        # if lower is 0 or nlen, sidx==eidx
        # otherwise pointer two consective pos
        sidx=0 if left==0 else left-1
        eidx=nlen-1 if left==nlen else left
    
        st=self._data[sidx]
        et=self._data[eidx]
        # 1.val already in data
        if st.start<=val and st.end>=val:
            return 
        if et.start<=val and et.end>=val:
            return 
        # 2.merge the interval,(1,1)(3,3), val==2
        if st.end+1==val and et.start-1==val:
            st.end=et.end
            self._data.pop(eidx)
            return 
        # 3. extend to start
        if st.end+1==val:
            st.end=val
            return
        # 4. extend to b
        if et.start-1==val:
            et.start=val
            return 
        
        # 5.insert to the pos
        self._data.insert(left,Interval(val,val))
        
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self._data
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()