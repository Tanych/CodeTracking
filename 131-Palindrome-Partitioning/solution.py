class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        n=len(s)
        for i in xrange(1,n+1):
            # if s[:i] is palindrome
            if s[:i]==s[i-1::-1]:
                # check the rest part
                for rest in self.partition(s[i:]):
                    res.append([s[:i]]+rest)
        return res if res else [[]]