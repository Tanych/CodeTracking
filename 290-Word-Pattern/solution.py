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
        # building pattern map    
        hashmap={}
        for i in xrange(len(pattern)):
            hashmap[pattern[i]]=hashmap.get(pattern[i],[])+[i]
        
        # check the intersection is equal
        intersection=[]
        for li in hashmap.values():
            intersection.append(li[0])
            # check in the same pattern
            for i in xrange(1,len(li)):
                if strlist[li[0]]!=strlist[li[i]]:
                    return False
        # if not in the same pattern , should not equal    
        for i in xrange(1,len(intersection)):
            if strlist[intersection[0]]==strlist[intersection[i]]:
                return False
        return True