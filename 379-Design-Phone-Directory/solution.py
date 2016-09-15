class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.maxnum=maxNumbers
        self.releasenum=[0]*maxNumbers
        self.flag=[True for _ in xrange(maxNumbers)]
        self.nextidx=self.ridx=0
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        # first try to get the number from the release
        if self.ridx<=0 and self.nextidx>=self.maxnum:
            return -1
        if self.ridx>0:
            self.ridx-=1
            res=self.releasenum[self.ridx]
            self.flag[res]=False
            return res
        # get from the available
        res=self.nextidx
        self.flag[res]=False
        self.nextidx+=1
        return res
        
    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0<=number<self.maxnum and self.flag[number]
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if 0<=number<self.maxnum and not self.flag[number]:
            self.releasenum[self.ridx]=number
            self.flag[number]=True
            self.ridx+=1
            
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)