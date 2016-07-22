class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        
        dirlist=path.split('/')
        
        resls=['/']
        for i in xrange(len(dirlist)):
            if dirlist[i]=='.' or dirlist[i]=='':
                continue
            # if '/' is not the only then pop
            if dirlist[i]=='..' and len(resls)>1:
                   resls.pop() 
            elif dirlist[i]!='..':
                resls.append('/'+dirlist[i])
        # if only has '/' directly reutrn ,otherwise get rid of the first
        return ''.join(resls if len(resls)==1 else resls[1:])