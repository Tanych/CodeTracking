class Solution(object):
    def wordPattern(self, pattern, strs):
        """
        :type pattern: str
        :type str: strs
        :rtype: bool
        """
        if not pattern and not strs:
            return True
            
        strlist=strs.split(" ")
        if len(strlist)!=len(pattern):
            return False
        # chars map
        charmap=[None]*26
        plist=list(pattern)
        while len(plist):
            string,ch=strlist.pop(),plist.pop()
            # get the index
            index=ord(ch)-97
            
            if charmap[index]!=string and charmap[index]:
                return False
            elif charmap[index]!=string and string in charmap:
                return False
            elif string not in charmap:
                charmap[index]=string
        return True
                
                