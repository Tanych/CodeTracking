class Solution(object):
    def strsort(self, s):
        cnt=[0]*26
        res=''
        for ch in s:
            cnt[ord(ch)-ord('a')]+=1
        for i in xrange(26):
            res+=str(ord('a')+i)*cnt[i]
        return res
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n=len(strs)
        hashmap={}
        for i in xrange(n):
            # sorted the key 
            key=self.strsort(strs[i])
            # if the key is the same plus
            hashmap[key]=hashmap.get(key,[])+[strs[i]]
        return [v for v in hashmap.values()]