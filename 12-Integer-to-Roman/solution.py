class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # first need check what's roman numeral
        # https://en.wikipedia.org/wiki/Roman_numerals
        int_map=[2000,1000, 900,500, 400, 200,100,  90, 50,  40,  20, 10,  9,   5,   4,   2,  1]
        roman_map=["MM", "M","CM","D","CD","CC","C","XC","L","XL","XX","X","IX","V","IV","II","I"]
        
        res=''
        idx=0
        n=len(int_map)
        
        while num>0:
            if num>=int_map[n-1-idx]:
                if num in
                num-=int_map[n-1-idx]
                res+=roman_map[n-1-idx]
            idx+=1
            
        return res