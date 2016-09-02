class Solution(object):
    def __init__(self):
        self.cnt=0
        
    def findhelper(self,low,high,word):
        if len(word)>=len(low) and len(word)<=len(high):
            if (len(word)==len(low) and word<low) or \
                (len(word)==len(high) and word>high):
                    return
            if not (len(word)>1 and word[0]=='0'):
                self.cnt+=1
        if len(word)+2>len(high):return
        self.findhelper(low,high,'0'+word+'0')
        self.findhelper(low,high,'1'+word+'1')
        self.findhelper(low,high,'6'+word+'9')
        self.findhelper(low,high,'8'+word+'8')
        self.findhelper(low,high,'9'+word+'6')
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.findhelper(low,high,'')
        self.findhelper(low,high,'0')
        self.findhelper(low,high,'1')
        self.findhelper(low,high,'8')
        return self.cnt
        