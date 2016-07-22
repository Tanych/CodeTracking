class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or not maxWidth:
            return [""]
        
        res=[]
        
        wlen=len(words)
        i=0
        while i<wlen:
            # get the total len for each line
            # get rid of the last space for each line
            # ex:This_is_an(_), we need get rid of the (_) after `an`
            sum_len=-1
            # start to count the number of words and the total length with one space 
            j=i
            while j<wlen and sum_len+len(words[j])+1<=maxWidth:
                sum_len+=len(words[j])+1
                j+=1
            
            """
            since we need to count the evenly distribution space and the extra space
            1. count the total space need to add(total_space)
            2. get the gaps between the words, the gaps can fill in (total_space/gaps) space
            3. add the extra space in the left gaps, in the previous `total_space%gaps` gaps
            L=20
            EX: We_are_family_ _ _ _ _ _ _  7/2=3 7%2=1 we_ _ _ _ _ are _ _ _ _family
            the first gap need feed one more
            """
            # the number that every gaps need fill,the default is 1,since need one space to seprate
            avgfill=1
            # the number of the left part gaps need to fill
            extrafill=0
            # since j reach the words can't be count, it shoud minus 1
            cntgaps=j-i-1
            
            # the gaps need fill more space
            # if only one word in one line, and not last line, we only jump to remaining
            # if don't and add j!=i+1 it's ok since the next for won't run
            if  j!=i+1 and j!=wlen:
                # the 1 is for the default seprate the words in previous step
                avgfill=(maxWidth-sum_len)/cntgaps+1
                extrafill=(maxWidth-sum_len)%cntgaps
            
            linres=words[i]
            for k in xrange(i+1,j):
                for m in xrange(avgfill):
                    linres+=' '
                # fill in the previous left
                if extrafill:
                    linres+=' '
                    extrafill-=1
                # go to next word
                linres+=words[k]
            
            # if we reach the last line,it might remain some space to fill
            # EX: the `justification`
            remain=maxWidth-len(linres)
            while remain:
                linres+=' '
                remain-=1
                
            # saving oneline result
            res.append(linres)
            # combine the even
            # restart the next line with j
            i=j
            
        return res
            