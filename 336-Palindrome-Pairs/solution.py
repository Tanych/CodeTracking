class Solution(object):
    def ispalindrome(self,strs):
        l,r=0,len(strs)-1
        while l<=r:
            if strs[l]==strs[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
        
        
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res=[]
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i==j:
                    continue
                if self.ispalindrome(words[i]+words[j]):
                    res.append([i,j])
        return res
                