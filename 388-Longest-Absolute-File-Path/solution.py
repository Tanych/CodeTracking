class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # the stck depth also indicate the depth of the dir
        stck,total,maxlen,i=[],0,0,0
        while i<len(input):
            # reach a new line
            if input[i]=='\n':
                i+=1
                begin=i
                # get the depth of the dir
                while input[i]=='\t':
                    i+=1
                # if reach a new higher subdir
                #-subdir1
                #--file1
                #-subdir2
                # when reach subdir2, the file1 and subdir2 need be deleted
                while len(stck)>(i-begin):
                    total-=stck.pop()
            else:
                begin=i
                isfile=False
                while i<len(input) and input[i]!='\n':
                    if input[i]=='.':
                        isfile=True
                    i+=1
                stck.append(i-begin)
                total+=stck[-1]
                if isfile:
                    # add number of '\'
                    maxlen=max(maxlen,total+len(stck)-1)
        return maxlen
                