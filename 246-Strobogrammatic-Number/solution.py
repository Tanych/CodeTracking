class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        special_num={'1':'1','6':'9','8':'8','9':'6','0':'0'}
        if len(num)==1:
            if num[0] in ['1','8','0']:
                return True
            else:
                return False
        
        for index in range(len(num)/2+1):
            if num[index] not in special_num:
                return False
            if num[len(num)-1-index] != special_num[num[index]]:
                return False
        return True
