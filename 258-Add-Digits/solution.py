class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=0
        while True:
            if num==0:
                if res<10:
                    break
                else:
                    num=res
                    res=0
            digit=num%10
            num=num/10
            res+=digit
        return res
            
            