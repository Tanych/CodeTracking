class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from copy import deepcopy
        if not words:
            return []
        word_len=len(words[0])
        total_len=len(words)*word_len
        # building map for words
        res=[]
        i=0
        hashmap={}
        for word in words:
            hashmap[word]=hashmap.get(word,0)+1
                
        while i+total_len<=len(s):
            j=i
            copy=deepcopy(hashmap)
            while j< i+total_len:
                # if not in the hash, break
                if s[j:word_len+j] not in copy:
                    break
                else:
                    # if find than check whether occurs before
                    if copy[s[j:word_len+j]]==1:
                        del copy[s[j:word_len+j]]
                    else:
                        # no, update the occurs
                        copy[s[j:word_len+j]]-=1
                j+=word_len
            # if all in hashmap and only occurs once, add to res
            if len(copy)==0:
                res.append(i)
            i+=1
        return res