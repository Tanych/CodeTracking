class Solution(object):
    def isvalid(self,s):
        n=len(s)
        if not n: return False
        val=int(s)
        if val>255:return False
        return n==len(str(val))
            
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12:
            return []
            
        def dfs(strs,step,path,res):
            if step==3:
                if self.isvalid(strs):
                    res.append(path+'.'+strs)
                    return
            for i in xrange(len(strs)):
                unit=strs[:i]
                if self.isvalid(unit):
                    divide='.' if path else ''
                    dfs(strs[i:],step+1,path+divide+unit,res)
                
        res=[]
        dfs(s,0,'',res)
        return res