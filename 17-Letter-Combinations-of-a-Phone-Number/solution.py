class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        def dfs(digits,step,path,res):
            if step==len(digits):
                if path!='':
                    res.append(path)
                return
            if step>len(digits):
                return
            for ch in mapping[int(digits[step])]:
                dfs(digits,step+1,path+ch,res)
        
        n=len(digits)
        if n==0:
            return []
        res=[]
        trimdigits=""
        for digit in digits:
            if digit!='0' and digit!='1':
                trimdigits+=digit
                
        for ch in mapping[int(trimdigits[0])]:
            dfs(trimdigits,1,""+ch,res)
            
        return res\
        