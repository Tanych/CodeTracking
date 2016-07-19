class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # for this problem, I think it really depends on 
        # the interviewers or the coding language
        # -.5 .0  0. .89 are all valid number in python
        # for the exponent, sometime 1e-.5 are also valid
        # need to record the following important state
        # hasE hasDot hasSign hasDigit
        
        
        # get rid of the whitespace
        start=0
        n=len(s)
        if n==0:
            return False
            
        s=s.strip()
        n=len(s)
        # no other return false
        if n==0:
            return False
        
        hasE=hasDot=hasSign=hasDigit=False
        
        while start<n:
            if s[start]>='0' and s[start]<='9':
                hasDigit=True
                hasSign=True
                
            # if previous has num or has the '+,-'
            elif s[start]=='+' or s[start]=='-':
                if hasSign:
                    return False
                hasSign=True
            
            elif s[start]=='e':
                # only one e possilbe and 
                # the number must before `e`
                if hasE or not hasDigit:
                    return False
                hasE=True
                # reset the digit and sign
                # since after `e` is a new valid number
                hasSign=False
                hasDigit=False
                # not reset . since 1e-0.5 1e-.2 are invalid in python
                # but we can reset if interview require
                hasDot=True
                    
            elif s[start]=='.':
                if hasDot:
                    return False
                hasDot=True
                # ".-4" if not possible
                hasSign=True
            else:
                return False
            
            start+=1
            
        return hasDigit
        