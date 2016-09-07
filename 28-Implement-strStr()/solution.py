class Solution(object):
    def searchsub(self,src,pattern):
        m=len(src)
        n=len(pattern)
        nextidx=[0]*(n+1)
        # get next pattern
        self.getNext(pattern,nextidx)
        j=0
        for i in xrange(m):
            while j>0 and src[i]!=pattern[j]:
                j=nextidx[j]
            if src[i]==pattern[j]:
                j+=1
            if j==n:
                return (i-j+1)
        return -1

    def getNext(self,pattern,nextidx):
        n=len(pattern)
        j=0
        for i in xrange(1,n):
            while j>0 and pattern[j]!=pattern[i]:
                j=nextidx[j]
            if pattern[j]==pattern[i]:
                j+=1
            nextidx[i+1]=j
            
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        return self.searchsub(haystack,needle)
        
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
