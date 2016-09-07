class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        i=0
        while i+len(needle)-1<len(haystack):
            hpos,npos=i,0
            while npos<len(needle) and haystack[hpos]==needle[npos]:
                hpos+=1
                npos+=1
            if npos==len(needle):
                return i
            i+=1
        return -1
