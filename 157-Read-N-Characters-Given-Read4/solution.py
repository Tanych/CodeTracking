# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i=0
        while i<n:
            tmp=[0]*4
            nlen=read4(tmp)
            for j in xrange(min(n-i,nlen)):
                buf[i+j]=tmp[j]
            if nlen<4:
                return min(i+nlen,n)
            i+=4
        return n
        