class Solution(object):
    def rle_decoding(self, strs):
        res_list, cnt_list, res_str, cnt, i = [], [], '', 0, 0
        while i < len(strs):
            if strs[i].isdigit():
                cnt=cnt*10+int(strs[i])
                i += 1
                continue
            else:
                j = i
                while j < len(strs) and not strs[j].isdigit():
                    j += 1
                res_list.append(strs[i:j])
                cnt_list.append(cnt)
                cnt = 0
                i = j
        for k in xrange(len(res_list)):
            res_str += res_list[k] * cnt_list[k]
        print res_str
        return res_str

    def decodeString(self, strs):
        """
        :type s: str
        :rtype: str
        """
        stck = []
        for i in xrange(len(strs)):
            if strs[i] == ']':
                tstr = []
                while stck and stck[-1] != '[':
                    tstr.insert(0,stck.pop())
                if stck:
                    # pop out the '['
                    stck.pop()
                    # add the number
                    while stck and stck[-1].isdigit():
                        tstr.insert(0,stck.pop())
                    # add to result
                    stck.append(self.rle_decoding(''.join(tstr)))
            else:
                stck.append(strs[i])
        return ''.join(stck) if stck else ''
        