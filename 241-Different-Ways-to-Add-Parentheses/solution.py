class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # naive recursivie
        mapping={}
        if input in mapping:
            return mapping[input]
            
        res=[]
        for i in xrange(len(input)):
            if not input[i].isdigit():
                for left in self.diffWaysToCompute(input[:i]):
                    for right in self.diffWaysToCompute(input[i+1:]):
                        if input[i]=='+':
                            res.append(left+right)
                        elif input[i]=='-':
                            res.append(left-right)
                        elif input[i]=='*':
                            res.append(left*right)
                mapping[input]=res
                
        return res if len(res) else [int(input)]
        