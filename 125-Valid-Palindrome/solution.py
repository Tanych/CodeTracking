class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        left,right=0,len(s)-1
        
        while left<right:
            while left<len(s) and not s[left].isalnum():
                left+=1
            while right>0 and not s[right].isalnum():
                right-=1
            if left<right:
                if s[left].lower()!=s[right].lower():
                    return False
                left+=1
                right-=1
        return True
            