class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # the newton interge
        # https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
        # it's short but not the cs way
        # i=num
        # while i*i>num:
        #     print i
        #     i=(i+num/i)/2
        # return i*i==num
        
        #in cs binary search
        # using two pointer to search betweent[1,num/2+1]
        
        begin,end=1,num/2+1
        while begin<end:
            mid=(begin+end)/2
            print mid
            sqt=mid*mid
            if num==sqt:
                return True
            elif num>sqt:
                begin=mid+1
            else:
                end=mid-1
                
        return begin*begin==num
        