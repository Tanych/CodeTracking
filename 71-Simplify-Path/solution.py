class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        
        dirlist=path.split('/')
        
        resstr=['/']
        for i in xrange(len(dirlist)):
            if dirlist[i]=='.' or dirlist[i]=='':
                continue
            if dirlist[i]=='..':
                if len(resstr)==1 and resstr[0]=='/':
                    continue
                else:
                   resstr.pop() 
            else:
                resstr.append('/'+dirlist[i])
        
        return ''.join(resstr if len(resstr)==1 else resstr[1:])