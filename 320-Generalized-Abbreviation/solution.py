class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res=['']
        
        for ch in word:
            tmp=[]
            for ele in res:
                tmp.append(ele+ch)
                if ele and ele[-1].isdigit():
                    tmp.append(ele[:-1]+str(int(ele[-1])+1))
                else:
                    tmp.append(ele+'1')
            res=tmp
        return res