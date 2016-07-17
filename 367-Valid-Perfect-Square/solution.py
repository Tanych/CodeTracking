class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # the newton interge
        # https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
        # it's short but not the cs way
        i=num
        while i*i>num:
            print i
            i=(i+num/i)/2
        return i*i==num