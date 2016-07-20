class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
            
        mapping=["","Thousand","Million", "Billion"]

        res=[0,0,0,0]
        i=0
        while num>0:
            res[i]=num%1000
            num=num/1000
            i+=1

        resstr=''
        for i in xrange(len(res)-1,-1,-1):
            if res[i]:
                resstr+=self.helperths(res[i])
                if mapping[i]:
                    resstr+=' '+mapping[i]+' '
        return resstr.strip()

    def helperths(self,num):
        """
        deal with the number less than one thousand
        """
        mapping={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
                 11:'Eleven',12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
                 30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}

        if num==0:
            return mapping[0]

        res=[0,0,0]
        i=0
        while num:
            digit=num%10
            num=num/10
            res[i]=digit
            i+=1

        resstr=''
        leftstr=''
        if res[-1]:
            resstr+=mapping[res[-1]]+' Hundred'
            
        tenvalue=res[-2]*10+res[-3]
        if 0<tenvalue<=20:
            leftstr+=mapping[res[-2]*10+res[-3]]
        elif tenvalue>20:
            leftstr+=mapping[res[-2]*10]
            if res[-3]:
                leftstr+=' '+mapping[res[-3]]
                
        if resstr and leftstr:
            return resstr+' '+leftstr
        elif resstr:
            return resstr
        elif leftstr:
            return leftstr
