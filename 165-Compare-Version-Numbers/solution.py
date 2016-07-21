class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        num1=version1.split('.')
        num2=version2.split('.')
        
        i,j=0,0
        while i<len(num1) and j<len(num2):
            if int(num1[i])>int(num2[j]):
                return 1
            elif int(num1[i])<int(num2[j]):
                return -1
            i+=1
            j+=1
    
        if i==len(num1) and  j==len(num2):
            return 0
        elif i==len(num1) and j<len(num2):
            while j<len(num2) and int(num2[j])==0:
                j+=1
            if j==len(num2):
                return 0
            return -1
        elif i<len(num1) and j==len(num2):
            while i<len(num1) and int(num1[i])==0:
                i+=1
            if i==len(num1):
                return 0
            return 1
     