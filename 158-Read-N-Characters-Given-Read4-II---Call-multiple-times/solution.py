# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.remain=[]
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i=0
        while i<n and self.remain:
            buf[i]=self.remain.pop(0)
            i+=1
        
        while i<n:
            tmp=[0]*4
            nlen=read4(tmp)
            if n-i<nlen:
                # copy buf needed
                j=0
                while j<n-i:
                    buf[i+j]=tmp[j]
                    j+=1
                # copy the left
                while j<nlen:
                    self.remain.append(tmp[j])
                    j+=1
            else:
                # copy all to the buf
                for j in xrange(nlen):
                    buf[i+j]=tmp[j]
            # return the min extra length
            if nlen<4:
                return min(i+nlen,n)
            i+=4
        return n
        