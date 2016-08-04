class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valset=[]
        # record the index to remove
        self.dictional={}
        self.index=0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            idx=self.dictional[val]
            return False
        except KeyError:
            self.valset.append(val)
            self.dictional[val]=self.index
            self.index+=1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            idx=self.dictional[val]
            self.valset[-1],self.valset[idx]=self.valset[idx], self.valset[-1]
            self.dictional[self.valset[idx]]=idx
            self.valset.pop()
            self.index-=1
            del self.dictional[val]
            return True
        except KeyError:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.valset[random.randint(0, len(self.valset)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()