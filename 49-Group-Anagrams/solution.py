class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n=len(strs)
        hashmap={}
        for i in xrange(n):
            # sorted the key 
            key=''.join(sorted(list(strs[i])))
            # if the key is the same plus
            hashmap[key]=hashmap.get(key,[])+[strs[i]]
        return [v for v in hashmap.values()]