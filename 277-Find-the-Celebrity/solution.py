# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate=0
        for i in xrange(n):
            # find the 'maxinum' candidate
            if knows(candidate,i):
                candidate=i
        # after candidate, the value all less than candidate
        # it means all the people beyond knows candidate
        # check whether before has large value, means
        # check whether has people candidate knows
        if any(knows(candidate,i) for i in xrange(candidate)): 
            return -1
        # check all know candidate
        if not all(knows(i,candidate) for i in xrange(n)):
            return -1
                
        return candidate
            