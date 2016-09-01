class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res=[]
        for s in strs:
            res.append(str(len(s))+':'+s)
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res=[]
        i=0
        while i<len(s):
            j=s.find(':',i)
            i=j+1+int(s[i:j])
            res.append(s[j+1:i])
        return res
        