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
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        n=len(word)
        if not n:
            return False
        curnode=self.root
        for i in xrange(n):
            pos=ord(word[i])-97
            if curnode.childlist[pos]:
                curnode=curnode.childlist[pos]
            else:
                return False
        # if reach the ends 
        return curnode.isend

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n=len(prefix)
        if not n:
            return False
        curnode=self.root
        for i in xrange(n):
            pos=ord(prefix[i])-97
            if curnode.childlist[pos]:
                curnode=curnode.childlist[pos]
            else:
                return False
                
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")