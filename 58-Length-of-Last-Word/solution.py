class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        res=s.split()
        return len(res[-1]) if res else 0