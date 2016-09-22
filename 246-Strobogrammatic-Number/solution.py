class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        special_num={'1':'1','6':'9','8':'8','9':'6','0':'0'}
        n=len(num)
        if n==1:
            if num[0] in ['1','8','0']:
                return True
            else:
                return False
        
        for i in xrange(n/2+1):
            if num[i] not in special_num:
                return False
            if num[n-1-i] != special_num[num[i]]:
                return False
        return True
