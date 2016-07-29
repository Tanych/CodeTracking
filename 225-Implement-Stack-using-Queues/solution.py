class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # can only has popleft
        import collections
        self.queue=collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        queue=self.queue
        queue.append(x)
        # revese
        for _ in xrange(len(queue)-1):
            queue.append(queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.queue)
        