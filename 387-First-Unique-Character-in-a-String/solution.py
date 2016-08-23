class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping=[0]*26
        for ch in s:
            mapping[ord(ch)-97]+=1
        print mapping
        