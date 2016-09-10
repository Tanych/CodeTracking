class Solution(object):
    def followup(self,s,k):
        """
        the question follow up is data char, only can read one char
        """
        if not s or k==0:
            return 0
        # using the maxheap to save the lastoccurence of the char
        maxheap=[]
        # window size record the k distince char
        inwindow={}
        j,maxlen=0,1
        # also can read char from the api
        for i in xrange(len(s)):
            ch=s[i]
            if len(inwindow)==k and (ch not in inwindow):
                idx,first=heapq.heappop(maxheap)
                del inwindow[first]
                j=idx+1
            if ch in inwindow:
                #del maxheap[-inwindow[ch]]
                for idx in xrange(len(maxheap)):
                    if maxheap[idx][1]==ch:
                        maxheap[idx],maxheap[-1]=maxheap[-1],maxheap[idx]
                        maxheap.pop()
                        heapq.heapify(maxheap)
                        break
            inwindow[ch]=i
            heapq.heappush(maxheap,(i,ch))
            maxlen=max(maxlen,(i-j+1))
        return maxlen
            
        
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.followup(s,k)
        strcnt=[0]*128
        res=cnt=left=right=0
        while right<len(s):
            if strcnt[ord(s[right])]==0:
                cnt+=1
            strcnt[ord(s[right])]+=1
            right+=1
            
            while cnt>k:
                if strcnt[ord(s[left])]==1:
                    cnt-=1
                strcnt[ord(s[left])]-=1
                left+=1
            res=max(res,right-left)
        return res
                