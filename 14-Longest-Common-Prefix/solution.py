class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
            
        res=""
        strs.sort()
        for i in xrange(len(strs[0])):
            if strs[0][i]==strs[-1][i]:
                res+=strs[0][i]
            else:
                break
        return res
