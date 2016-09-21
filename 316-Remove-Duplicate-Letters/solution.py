class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_dict={}
        stck=[]
        str_len=len(s)
        if str_len<=1:
            return s
        
        for i in xrange(str_len):
            hash_dict[s[i]]=hash_dict.get(s[i],0)+1

        for i in xrange(str_len):
            # alredy in
            if s[i] in stck:
                hash_dict[s[i]]-=1
                continue
            while stck and s[i]<=stck[-1] and hash_dict[stck[-1]]>1:
                hash_dict[stck[-1]]-=1
                stck.pop()
            stck.append(s[i])
        return ''.join(stck)
                
            