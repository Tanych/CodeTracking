class Solution(object):
    def __init__(self):
        # 1-{0,1,8} 2-{00,11,69,88,96}
        self.cntmemo = {-1: 1, 0: 1, 1: 3, 2: 5}
        # mapping the corresponding number
        self.mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

    def count_same_len(self, str_num):
        slen = len(str_num)
        spos, pstr = 0, slen
        rescnt = 0
        # record equal cnt when compare with the target
        lesscnt = 0
        while pstr > 0:
            if slen == 1 or pstr == 1:
                candidates = (0, 1, 8)
            # first digital get rid of 0
            elif pstr == slen:
                candidates = (1, 6, 8, 9)
            else:
                candidates = (0, 1, 6, 8, 9)
            for num in candidates:
                # if the number less than the target,add all the possible in strlen-2
                if num < int(str_num[spos]):
                    rescnt += self.cntmemo[pstr - 2]
                # if equal we need to record, util to the middle compare
                elif num == int(str_num[spos]):
                    # if the mapping pos num less or equal to the target, it's possible
                    if self.mapping[num] <= int(str_num[slen-1-spos]):
                        # record the less cnt
                        lesscnt += 1
                        # if match on the middle, it means this number can fit
                        # 89768 match 89789, 8,9 all equal 6<8 and 8<9, two counts
                        if pstr < 3 and lesscnt == (slen + 1) / 2:
                            rescnt += 1
                    break
                else:
                    return rescnt
            pstr -= 2
            spos += 1
        return rescnt
    
    def count_less_than(self, str_num):
        rescnt, slen = 0, len(str_num)
        # count the number less than str_num with length less than str len
        if int(str_num) < 0: return 0
        if slen > 1:
            # get rid of 0, it's 4/5 of all the total.
            rescnt = 3 + sum([self.cntmemo[i] for i in xrange(2,slen)]) * 4 / 5
        # count the number with the same length
        return rescnt+self.count_same_len(str_num)

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high):
            return 0
        # count all larger than 2
        for i in xrange(3, len(high)):
            self.cntmemo[i] = self.cntmemo[i - 2] * 5
        return self.count_less_than(high) - self.count_less_than(str(int(low)-1))
    
        