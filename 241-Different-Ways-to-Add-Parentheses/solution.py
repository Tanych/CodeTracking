class Solution(object):
    def diffWaysToCompute(self,input):
        """
        define dp[i][j] is the result from the expression from i to j
        dp[j][j]=input[j] for j in odd position
        """
        import re
        input = re.split('(\+|\-|\*|\/)', input)
        n=len(input)
        dp=[[[] for _ in xrange(n)] for _ in xrange(n)]
        
        # i means the total length of the expression
        # EX: 3-4*5+6*7, i=3, there could be 3-4,4*5,5+6,6*7.
        for i in xrange(1,n+1,2):
            # start from num j, it could be the total possible expression based on the length of i
            # so j need stop at the length of n-i+1, to make sure the last has i length
            for j in xrange(0,n+1-i,2):
                # the total length of expression could be 1, and it only should contains numbers
                if i==1:
                    dp[j][j+i-1].append(eval(input[j]))
                else:
                    # k could be the operator in all the possible expression
                    # if from i,j the expression is  3-4*5+6*7, k could be - ,* ,+,*
                    # for the i length expression, the last op is j+i-1
                    for k in xrange(j+1,j+i-1,2):
                        left=dp[j][k-1]; right=dp[k+1][j+i-1];
                        for num1 in left:
                            for num2 in right:
                                dp[j][j+i-1].append(eval(str(num1)+input[k]+str(num2)))
        return dp[0][n-1]
                        
        
    def diffWaysToCompute_rec(self, input):
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

        