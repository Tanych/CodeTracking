class Solution(object):
    def python2(self,input):
        total,maxlen,stck=0,0,[]
        for line in input.split('\n'):
            pathname=line.lstrip('\t')
            depth=len(line)-len(pathname)
            # if reachs previous higher subdir,pop the deeper ones
            while len(stck)>depth:
                total-=stck.pop()
            stck.append(len(pathname))
            total+=stck[-1]
            # if reaches path end
            if '.' in pathname:
                maxlen=max(maxlen,total+len(stck)-1)
        return maxlen
            
    def pythonway(self,input):
        path={0:0}
        maxlen=0
        for line in input.split('\n'):
            name=line.lstrip('\t')
            depth=len(line)-len(name)
            if '.' in name:
                maxlen=max(maxlen,path[depth]+len(name))
            else:
                path[depth+1]=path[depth]+len(name)+1
        return maxlen
        
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        return self.python2(input)
        
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
                