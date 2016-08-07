class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_num=0
        mapping={}
        
        for word in words:
            pre_intmark=0
            for ch in set(word):
                pre_intmark|=1<<(ord(ch)-97)
            # save the max with the same letter
            mapping[pre_intmark]=max(mapping.get(pre_intmark,0),len(word))
        
        for x in mapping:
            for y in mapping:
                if not x&y:
                    if max_num<mapping[x]*mapping[y]:
                        max_num=mapping[x]*mapping[y]
        return max_num