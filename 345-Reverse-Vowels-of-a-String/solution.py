class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        mapping=['a','e','i','o','u','A','E','I','O','U']
        
        left,right=0,len(s)-1
        
        while left<right:
            while left<len(s) and s[left] not in mapping:
                left+=1
            while right>0 and s[right] not in mapping:
                right-=1
                
            if left<right:
                s=s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]
                left+=1
                right-=1
        return s
        