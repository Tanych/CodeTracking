class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        res=''
        i,j=len(a)-1,len(b)-1
        while i>=0 and j>=0:
            val=int(a[i])+int(b[j])+carry
            tval=val%2
            carry=val/2
            res+=str(tval)
            i-=1
            j-=1
        
        while i>=0:
            val=int(a[i])+carry 
            tval=val%2
            carry=val/2
            res+=str(tval)
            i-=1
        while j>=0:
            val=int(b[j])+carry 
            tval=val%2
            carry=val/2
            res+=str(tval)
            j-=1
        # if the lastone has carry
        if carry:
            res+=str(carry)
            
        return res[::-1]