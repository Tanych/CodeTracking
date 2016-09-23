class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res,remainmap="",{}
        
        isneg=True if numerator*denominator<0 else False
        if numerator<0:
            numerator*=-1
        if denominator<0:
            denominator*=-1
        
        str_before=str(numerator/denominator)
        remain=numerator%denominator

        str_after=""
        while remain!=0:
            numerator=remain*10
            str_after+=str(numerator/denominator)
            # get the repeate index
            remainmap[remain]=len(str_after)-1
            remain=numerator%denominator

            if remain in remainmap:
                break
        # if has the repeat result
        if remain:
            remain_start=remainmap[remain]
            str_after=str_after[:remain_start]+'('+str_after[remain_start:]+')'
        #combine the result
        if isneg:
            res='-'
        if str_after=="":
            res+=str_before
        else:
            res+=str_before+'.'+str_after
        return res