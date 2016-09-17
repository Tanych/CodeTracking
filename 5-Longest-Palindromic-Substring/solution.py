class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        str_len=len(s)
        longest=s[0]
        for i in range(str_len-1):
            p1=self.expandfromcenter(s,i,i)
            if len(p1)>len(longest):
                longest=p1
                
            p2=self.expandfromcenter(s,i,i+1)
            if len(p2)>len(longest):
                longest=p2
                
        return longest
    
    def expandfromcenter(self,s,c1,c2):
        left=c1
        right=c2
        str_len=len(s)
        while left>=0 and right<=str_len-1 and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    

    
    
    