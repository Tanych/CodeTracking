class Solution(object):
    def rearrangeString(self, strs, k):
        """
        :type str: strs
        :type k: int
        :rtype: strs
        """
        if k==0: return strs
        n=len(strs)
        maxheap=[]
        cnt=[0]*26
        for ch in strs:
            cnt[ord(ch)-97]+=1
        res=[]
        # building max heap
        for i in xrange(26):
            if cnt[i]:
                heapq.heappush(maxheap,(-cnt[i],chr(i+97)))
        
        while maxheap:
            # record the remaining
            remaining=[]
            t=min(k,n)
            for i in xrange(t):
                if not maxheap: return ""
                ct,ch=heapq.heappop(maxheap)
                res.append(ch)
                tcnt=-ct-1
                if tcnt:
                    remaining.append((-tcnt,ch))
                # mark the left length
                n-=1
                
            for ele in remaining:
                heapq.heappush(maxheap,ele)
                
        return ''.join(res)
        