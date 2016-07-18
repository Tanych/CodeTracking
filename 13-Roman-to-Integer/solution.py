class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the special is 1,4,5,9
        roman_map={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        
        n=len(s)
        if n==0:
            return 0
        i=0
        res=0
        while i<n:
            if i+1<n and s[i:i+2] in roman_map:
                res+=roman_map[s[i:i+2]]
                i+=2
                continue
            if s[i] in roman_map:
                res+=roman_map[s[i]]
                i+=1
                continue
           
        return res
            
        
        