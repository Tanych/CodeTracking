class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instck=[]
        self.outstck=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instck.append(x)
  
    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        return self.outstck.pop() 

    def peek(self):
        """
        :rtype: int
        """
        if not self.outstck:
            while self.instck:
                self.outstck.append(self.instck.pop())
        return self.outstck[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.instck) and not len(self.outstck)
        