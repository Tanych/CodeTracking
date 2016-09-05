class Solution(object):
    def inttobin(self,num):
        res=bin(num)[2:]
        if len(res)<=8:
            return '0'*(8-len(res))+res
        else:
            return res[-8:]
            
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        intbit=map(self.inttobin,data)
        i=0
        while i<len(intbit):
            if intbit[i].startswith('0'):
                i+=1
                continue
            onecnt=0
            while onecnt<len(intbit[i]) and intbit[i][onecnt]!='0':
                onecnt+=1
            # if has only one bit start,invalid
            if onecnt==1:
                return False
            # check the n-1 is 10 start
            for k in xrange(onecnt-1):
                if i+1+k>len(intbit)-1 or (not intbit[i+1+k].startswith('10')):
                    return False
            i+=onecnt
            
        return True    
        