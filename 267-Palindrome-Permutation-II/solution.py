class Solution(object):
    def helper(self,candidates,path,res):
        if not candidates:
            if path not in res:
                res.append(path)
            return
        for i in xrange(len(candidates)):
            self.helper(candidates[:i]+candidates[i+1:],path+candidates[i],res)
            
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        chcnt=[0]*128
        for ch in s:
            chcnt[ord(ch)]+=1
            
        candidates,oddnum,oddchar=[],0,''
        for i in xrange(128):
            if not chcnt[i]:
                continue
            if not chcnt[i]%2:
                candidates.extend([chr(i) for _ in xrange(chcnt[i]/2)])
            else:
                oddnum+=1
                if oddnum>1:
                    return []
                if chcnt[i]>1:
                    candidates.extend([chr(i) for _ in xrange((chcnt[i]-1)/2)])
                oddchar=chr(i)
                
        for i in xrange(len(candidates)):
            self.helper(candidates[:i]+candidates[i+1:],candidates[i],res)
            
        return [s+oddchar+s[::-1] for s in res] if res else [oddchar*chcnt[ord(oddchar)]]
        