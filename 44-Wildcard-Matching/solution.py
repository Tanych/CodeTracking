class Solution(object):
    def isMatch(self, src, dst):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        "the src string are just only for letter to match"
        
        """
        For each element in s
        If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
        If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
        If not match, then we check if there is a * previously showed up,
               if there is no *,  return false;
               if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.
        
        e.g.
        
        abefghdd
        ?b*d
        
        a=?, go on, b=b, go on,
        e=*, save * position star=3, save s position ss = 3, p++
        e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
        d=d, go on, meet the end.
        check the rest element in p, if all are *, true, else false;
        """
        sp,dp,asterick,matchstarpos=0,0,-1,0
        while sp<len(src):
            #if single ? match, just go on
            if dp<len(dst) and (src[sp]==dst[dp] or dst[dp]=='?'):
                dp+=1
                sp+=1
                continue
            #if match a '*', the situation becomes complex
            if dp<len(dst) and dst[dp]=='*':
                #record the star position
                asterick=dp
                #record the src star position
                matchstarpos=sp
                dp+=1
                continue
            #if not match,go to check the start, to restart a match
            if asterick!=-1:
                #if get a start,need restart to compare
                dp=asterick+1
                #go on to find the match char
                matchstarpos+=1
                #get back the match pos of src
                sp=matchstarpos
                continue
            return False
    
        #check the left dst whether all *
        while dp<len(dst) and dst[dp]=='*':
            dp+=1
    
        return dp==len(dst)