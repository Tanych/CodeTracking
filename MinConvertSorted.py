# given a string of a,b, a can convert to b, b can convert to a, also can do nothing.
# get the minumum of step to convert a sorted string.
class solution(object):
    def convertsorted(self,s):
        n=len(s)
        if n<=1: return n
        #endA[i] ends with a in i, endB ends with b
        endA,endB=[0]*(n+1),[0]*(n+1)
        for i in xrange(1,n+1):
            # if [i-1]=='a' endA no need op
            # endB need put a-->b from last endA[i-1] or endB[i-1]
            if s[i-1]=='a':
                endA[i]=endA[i-1]
                endB[i]=1+min(endA[i-1],endB[i-1])
            else:
                # if equal b, endA only needs to makes b-->a
                endA[i]=1+endA[i-1]
                endB[i]=min(endA[i-1],endB[i-1])
        print endA,endB
        return min(endA[n],endB[n])
s=solution()
print s.convertsorted('bbbaa')
