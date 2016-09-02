class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hash_dict={}
        if not strings:
            return []
        for sub in strings:
            key=self.hash_key(sub)
            hash_dict[key]=hash_dict.get(key,[])+[sub]
        return map(sorted,hash_dict.values())
    
    def hash_key(self,strs):
        """
        Produce the hash key with tuple list
        """
        key=[]
        for ch in strs:
            idx=(ord(ch)-ord(strs[0]))%26
            key.append(idx)
        return tuple(key)
        
        