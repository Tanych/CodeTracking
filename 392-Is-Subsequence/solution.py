class Solution(object):
    def manys(self,s,t):
        hmaping={}
        # pre record the position
        for i in xrange(len(t)):
            hmaping[t[i]]=hmaping.get(t[i],[])+[i]
        
        # search index
        curidx=-1
        for ch in s:
            if ch not in hmaping or hmaping[ch][-1]<=curidx:
                return False
            left,right=0,len(hmaping[ch])-1
            while left<right:
                mid=(left+right)/2
                if hmaping[ch][mid]>curidx:
                    right=mid
                else:
                    left=mid+1
            curidx=hmaping[ch][left]
        return True
                
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.manys(s,t)
        sidx=tidx=0
        while sidx<len(s) and tidx<len(t):
            if s[sidx]==t[tidx]:
                sidx+=1
            tidx+=1
        return sidx==len(s)
        
        i=0
        for ch in s:
            newi=t.find(ch,i)
            if newi==-1:return False
            i=newi+1
        return True