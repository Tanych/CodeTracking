class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # there are lots of coner case to deal with
        # 01.1 9.0.0 vs 9 9.000.0vs 9 
        i,j=0,0
        n1,n2=len(version1),len(version2)
        while i<len(version1) or j<len(version2):
            intv1,intv2=0,0
            # the num in version1
            while i<n1 and version1[i]!='.':
                intv1=intv1*10+int(version1[i])
                i+=1
            # the number in version2
            while j<n2 and version2[j]!='.':
                intv2=intv2*10+int(version2[j])
                j+=1
                
            # compare
            if intv1>intv2:
                return 1
            elif intv1<intv2:
                return -1
            # if eqaul move on next level
            i+=1
            j+=1
     
        return 0
    