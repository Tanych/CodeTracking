class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        strnums=[]
        for num in nums:
            strnums.append(str(num))
        
        # sorted as string
        strnums.sort(lambda x,y:int(y+x)-int(x+y))
        
        res=''.join(strnums)
        # get rid of the first 0
        while len(res)>1 and res[0]=='0':
            res=res[1:]
        return res
        