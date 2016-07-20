class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        left,right=0,len(s)-1
        
        lis=list(s)
        
        while left<right:
            lis[left],lis[right]=lis[right],lis[left]
            left+=1
            right-=1
        
        return ''.join(lis)