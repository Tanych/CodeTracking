class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        res_note=[0]*128
        res_mag=[0]*128
        for ch in ransomNote:
            res_note[ord(ch)]+=1
        for ch in magazine:
            res_mag[ord(ch)]+=1
        
        for i in xrange(128):
            res_mag[i]-=res_note[i]
            if res_mag[i]<0: return False
        
        return True