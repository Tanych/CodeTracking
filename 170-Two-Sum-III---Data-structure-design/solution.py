class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.number=set()
        self.mapping={}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.mapping[number]=self.mapping.get(number,0)+1
        self.number.add(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.number:
            target=value-num
            if target in self.mapping:
                if target==num and self.mapping[target]<2:
                    continue
                return True
        return False
        
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)