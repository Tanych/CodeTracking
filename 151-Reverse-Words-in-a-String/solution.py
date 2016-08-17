class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        stck=[]
        tstr=''
        res=''
        for i in xrange(len(s)):
            if s[i]==' ':
                # for the continous space skip
                if not tstr:continue
                stck.append(tstr)
                tstr=''
            else:
                tstr+=s[i]
        # the last possible string
        if tstr:
            stck.append(tstr)
        
        while stck:
            res+=stck.pop()+' '
        
            
        return res[:-1]
        
            