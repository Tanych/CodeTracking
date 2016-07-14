class Solution(object):
    def contains(self,s,t):
        """
        case sensitive
        """
        cnt=[0]*52
        for ch in s:
            cnt[ord(ch)-ord('a')]+=1
            
        for ch in t:
            cnt[ord(ch)-ord('a')]-=1
            
        for i in xrange(52):
            if cnt[i]<0:
                return False
        return True
        
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # brute force
        st=''.join(sorted(t))
        minlen=1<<31-1
        res=''
        for i in xrange(len(s)):
            for j in xrange(i+len(t)-1,min(len(s),minlen+i+len(t)-1)):
                if self.contains(s[i:j+1],st):
                    if j-i<=minlen:
                        minlen=j-i
                        res=s[i:j+1]
        return res
    