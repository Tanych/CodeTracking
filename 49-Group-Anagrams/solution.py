class Solution(object):
    def key(self, s):
        INT_MAX=2<<31-1
        result=1
        for ch in s:
            n=ord(ch)-ord('a')+1
            result*=(n*n+n+41)%INT_MAX
        return result
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n=len(strs)
        hashmap={}
        for i in xrange(n):
            # sorted the key 
            key=self.key(strs[i])
            # if the key is the same plus
            hashmap[key]=hashmap.get(key,[])+[strs[i]]
        return [v for v in hashmap.values()]