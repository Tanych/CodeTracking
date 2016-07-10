class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # more pythonic way to do so
        if not digits:
            return []
        results = ['']
        mapping = {'0':'', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        for digit in digits:
            candiate=mapping[digit]
            tmp=[]
            for ch in candiate:
                for resch in results:
                    tmp.append(resch+ch)
            results,tmp=tmp,results
            
        return results
        