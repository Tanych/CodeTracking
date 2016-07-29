class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        stack=self.stack
        stack.appendleft(x)
  
    def pop(self):
        """
        :rtype: nothing
        """
        return self.stack.pop() 

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.stack)