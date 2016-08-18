class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap,tmap={},{}
        for i in xrange(len(s)):
            if s[i] not in smap:
                smap[s[i]]=len(smap)+1
            sint=smap[s[i]]
            
            if t[i] not in tmap:
                tmap[t[i]]=len(tmap)+1
            tint=tmap[t[i]]
            
            if sint!=tint:
                return False
        return True
        