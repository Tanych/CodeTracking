class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[1<<31]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.minstack[-1]>=x:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            if self.stack[-1]==self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()
            
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minstack)==1:
            return -1
        else:
            return self.minstack[-1]
            
        