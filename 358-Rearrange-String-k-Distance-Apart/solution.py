class Solution(object):
    def rearrangeString(self, strs, k):
        """
        :type str: strs
        :type k: int
        :rtype: strs
        """
        n=len(strs)
        maxheap=[]
        cnt=[0]*26
        for ch in strs:
            cnt[ord(ch)-97]+=1
        res=[]
        # building max heap
        for i in xrange(26):
            heapq.heappush(maxheap,(-cnt[i],chr(i+97)))
        
        while len(res)<n:
            # record the remaining
            remaining=[]
            t=min(k,n)
            for i in xrange(t):
                if not maxheap: return ""
                cnt,ch=heapq.heappop(maxheap)
                res.append(ch)
                tcnt=-cnt-1
                if tcnt:
                    remaining.append((-tcnt,ch))
            for ele in remaining:
                heapq.heappush(maxheap,ele)
                
        return ''.join(res)
        