class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # recursive to solve the problem
        # if empty pattern
        if not p:
            return not s
        
        # if the last is '*'
        if p[-1]=='*':
            # abcdeeee
            # abcde*
            if s and (s[-1]==p[-2] or p[-2]=='.'):
                # * match 0==>match(s,p[:-2])
                # * match 1 or more==>match preivous s and whole p
                return self.isMatch(s,p[:-2]) or self.isMatch(s[:-1],p)
            else:
                # abcdf
                # abcdfe*
                # only try to match abcdf abcdf
                return self.isMatch(s,p[:-2])
        else:
            # abcde
            # abcd.(e)
            if s and (s[-1]==p[-1] or p[-1]=='.'):
                return self.isMatch(s[:-1],p[:-1])
            else:
                # other return false
                return False
            
        
            
            