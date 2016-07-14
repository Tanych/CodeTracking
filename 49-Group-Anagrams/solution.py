class Solution(object):
    def isAnagram(self, s, t):
        chars=[0]*26
        for i in xrange(len(s)):
            chars[ord(s[i])-97]+=1
        for i in xrange(len(t)):
            chars[ord(t[i])-97]-=1
        for nums in chars:
            if nums!=0:
                return False
        return True
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n=len(strs)
        res=[]
        # record the pop index
        index=[]
        for i in xrange(n):
            # if previous access, pass
            if i in index:
                continue
            index.append(i)
            res.append([strs[i]])
            for j in xrange(i+1,n):
                # if previous pop, pass
                if j in index:
                    continue
                # check if anagram
                if self.isAnagram(strs[i],strs[j]):
                    index.append(j)
                    res[-1].append(strs[j])
        return res