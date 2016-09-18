class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num>10:
            return []
        hours,minutes={},{}
        for i in xrange(0,12):
            cnt=bin(i).count("1")
            hours[cnt]=hours.get(cnt,[])+[str(i)]
            
        for i in xrange(0,60):
            cnt=bin(i).count("1")
            minutes[cnt]=minutes.get(cnt,[])+['0'+str(i) if i<10 else str(i)]
            
        res=[]
        for i in xrange(0,min(4,num+1)):
            hour=hours[i] if i in hours else []
            mins=minutes[num-i] if num-i in minutes else []
            for h in hour:
                for m in mins:
                    res.append(h+':'+m)
        return res
