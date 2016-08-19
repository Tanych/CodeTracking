class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childlist=[0 for _ in xrange(26)]
        # the node value
        self.val=None
        # end flag to determin whether it's prefix
        self.isend=False
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root=TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word:
            return 
        
        curnode=self.root
        for i in xrange(len(word)):
            pos=ord(word[i])-97
            if not curnode.childlist[pos]:
                curnode.childlist[pos]=TrieNode()
                curnode.childlist[pos].val=word[i]
            # move on
            curnode=curnode.childlist[pos]
        curnode.isend=True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._query(word,self.root)
      
    
    def _query(self,word,root):
        curnode=root
        n=len(word)
        for i in xrange(n):
            # if not '.' just move to next level
            if curnode and word[i]!='.':
                curnode=curnode.childlist[ord(word[i])-97]
            # deal with '.'
            elif curnode and word[i]=='.':
                tmp=curnode
                for j in xrange(26):
                    curnode=tmp.childlist[j]
                    if self._query(word[i+1:],curnode):
                        return True
            else:
                break
        # check whether it search on the end
        if curnode:
            return  True and curnode.isend
        else:
            return False
                    
            
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")