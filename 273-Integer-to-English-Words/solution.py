class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
            
        mapping=["","Thousand","Million", "Billion"]

        resstr=''
        for i in range(len(mapping)):
            if num%1000 != 0:
                resstr = self.helperths(num%1000) + mapping[i] + ' ' + resstr
            num /= 1000
        return resstr.strip()

    def helperths(self,num):
        """
        deal with the number less than one thousand
        """
        lesstw = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
        if num==0:
            return ""
        if 0<num<20:
            return lesstw[num]+' '
        if 20<=num<100:
            return tens[num/10]+' '+self.helperths(num%10)
        if num>=100:
            return lesstw[num/100]+' Hundred '+self.helperths(num%100)
       
