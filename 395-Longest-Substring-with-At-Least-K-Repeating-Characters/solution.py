class Solution(object):
    def pythonic(self,s,k):
        if len(s)<k:
            return 0
        minchar=min(set(s),key=s.count)
        if s.count(minchar)>=k:
            return len(s)
        return max(self.pythonic(t,k) for t in s.split(minchar))
        
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.pythonic(s,k)
        charcnt=[0]*26
        charset=set()
        
        for ch in s:
            charcnt[ord(ch)-97]+=1
            if ch not in charset:
                charset.add(ch)
        for i in xrange(26):
            if charcnt[i]>=k:
                charset.discard(chr(i+97))
        if not charset:
            return len(s)
        splits,sp=[],0
        while sp<len(s):
            if s[sp] not in charset:
                i=sp
                while sp<len(s):
                    if s[sp] not in charset:
                        sp+=1
                    else:
                        break
                splits.append((i,sp))
            else:
                sp+=1
        maxlen=0
        for ele in splits:
            maxlen=max(maxlen,self.longestSubstring(s[ele[0]:ele[1]],k))
        return maxlen
                