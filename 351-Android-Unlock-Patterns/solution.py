class Solution(object):
    def __init__(self):
        self.jumps=[[0 for _ in xrange(10)] for _ in xrange(10)]
        self.jumps[1][3]=self.jumps[3][1]=2
        self.jumps[3][9]=self.jumps[9][3]=6
        self.jumps[1][7]=self.jumps[7][1]=4
        self.jumps[7][9]=self.jumps[9][7]=8
        self.jumps[2][8]=self.jumps[8][2]=self.jumps[4][6]=self.jumps[6][4]=5
        self.jumps[1][9]=self.jumps[9][1]=self.jumps[3][7]=self.jumps[7][3]=5
        self.visited=[False]*10
        
    def helper(self,num,remaining):
        if remaining<0: return 0
        if remaining==0: return 1
        self.visited[num]=True
        ret=0
        for i in xrange(1,10):
            jump=self.jumps[num][i]
            if not self.visited[i] and (not jump or self.visited[jump]):
                ret+=self.helper(i,remaining-1)
        self.visited[num]=False
        return ret
                
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=0
        for i in xrange(m,n+1):
            res+=self.helper(1,i-1)*4
            res+=self.helper(2,i-1)*4
            res+=self.helper(5,i-1)
        return res
            