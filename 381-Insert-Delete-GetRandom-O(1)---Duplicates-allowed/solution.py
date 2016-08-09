class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # saving the data
        self.data=[]
        # saving the index 
        self.idxdict={}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data.append(val)
        if val in self.idxdict:
            self.idxdict[val].append(len(self.data)-1)
            return False
        else:
            self.idxdict[val]=self.idxdict.get(val,[])+[len(self.data)-1]
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.idxdict: return False
        # get index list
        idx=self.idxdict[val].pop()
        if len(self.idxdict[val])==0: del self.idxdict[val]
        
        if idx!=len(self.data)-1:
            lastval=self.data[-1]
            lastq=self.idxdict[lastval]
            lastq.pop()
            # add the index to last element
            self.idxdict[lastval].append(idx)
            # swap idx and last index
            self.data[idx],self.data[-1]=self.data[-1],self.data[idx]
            
        # pop last element
        self.data.pop()
        return True
        
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.data[random.randint(0, len(self.data)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()