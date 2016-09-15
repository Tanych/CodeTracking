class Solution(object):
    def manys(self,s,t):
        hmaping=[[] for _ in range(26)]
        # pre record the position
        for i in xrange(len(t)):
            hmaping[ord(t[i])- 97].append(i)
        
        # search index
        curidx=-1
        for ch in s:
            if not hmaping[ord(ch)-97] or hmaping[ord(ch)-97][-1]<=curidx:
                return False
            left,right=0,len(hmaping[ord(ch)-97])-1
            while left<right:
                mid=(left+right)/2
                if hmaping[ord(ch)-97][mid]>curidx:
                    right=mid
                else:
                    left=mid+1
            curidx=hmaping[ord(ch)-97][left]
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