class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lrudict={}
        self.keylist=[]
        self.maxsize=capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.lrudict:
            return -1
        self.keylist.remove(key)
        self.keylist.append(key)
        return self.lrudict[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.lrudict:
            self.keylist.remove(key)
        elif len(self.lrudict)==self.maxsize:
            v=self.keylist.pop(0)
            self.lrudict.pop(v)
        self.keylist.append(key)
        self.lrudict[key]=value
        