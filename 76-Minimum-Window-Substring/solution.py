class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hmap=[0]*128
        # building map
        for ch in t:
            hmap[ord(ch)]+=1
        # using count to record the count balance
        minstart,start,end,count=0,0,0,len(t)
        # to ge the min lenght of the windows
        minlen=2<<31-1
        
        while end<len(s):
            # if s[end] exsit in hmap,
            # reduce the balance since it found
            if hmap[ord(s[end])]>0:
                count-=1
            # otherwise, if it not exist,reduce the value it would be negative
            hmap[ord(s[end])]-=1
            # move on find next 
            end+=1
            
            # if all target include
            while count==0:
                # get the min length
                if end-start<minlen:
                    # mark the start position
                    minstart=start
                    minlen=end-start
                # move start to find the min len
                # if the char in target, we passed the target element, 
                # need to find in the end pos,it should add balance for end to find
                # rollback the value to start move on
                hmap[ord(s[start])]+=1
                if hmap[ord(s[start])]>0:
                    count+=1
                # move on
                start+=1
        return "" if minlen==2<<31-1 else s[minstart:minstart+minlen]
        
        