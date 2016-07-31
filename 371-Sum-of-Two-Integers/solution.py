class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """
        for the bin add, we need to consider the following:
        1. carry
        2. overflow
        3. 32-bit int and 64-bit int
        4. python deal int as 64bit, java and c++ deal with 32bit
        """
        
        # set mask and flag to deal with 64 with 32 
        # (1<<31)-1
        MAX_32=0x7FFFFFFF
        #-(1<<31)
        MIN_32=0x80000000
        # 32 inter mask
        mask=0xFFFFFFFF
        """
        proof: a^b if there are not carry, it's directly the result of a+b
        EX: (1+2)-->01+10
        if there are carry, we need get the carry first,carry=(a&b)<<1, 
        so the final with carry is a^b+(a&b)<<1
        EX: (3+1)--(11+01)
        """
        ans=(a^b)&mask
        carry=((a&b)<<1)&mask
        while carry:
            # a get the single '1', b get the carry
            # 011,011-->b=110
            #a,b=(a^b)&mask,((a&b)<<1)&mask
            tmp=(ans^carry)&mask
            carry=((ans&carry)<<1)&mask
            ans=tmp
        
        # if a didn't overflow, directly return else
        """
        suppose the result would be -2 , after the previous op
        it get the res of 32-bit(0x00000000FFFFFFFE), 
        but python need the 64-bit -2(0xFFFFFFFFFFFFFFFE)
        what we do is getting the complement first 0x0000000000000001
        and then get the reverse 0x0xFFFFFFFFFFFFFFFE
        """
        return ans if ans<=MAX_32 else ~(ans^mask)
            