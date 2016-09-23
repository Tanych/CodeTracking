class TrieNode(object):
    def __init__(self):
        self.childlist=[None]*26
        self.val=None
        
class Solution(object):
    def dfs(self,board,root,i,j,res):
        original=board[i][j]
        # if can't find the prefix
        if original=='*' or not root.childlist[ord(original)-97]:
            return 
        
        pNode=root.childlist[ord(original)-97]
        # if reach the end add the word
        if pNode.val:
            res.append(pNode.val)
            pNode.val=None
            # if here return
            # we can't get the words with same prefix
            # such ben bena benf,only get ben
        # move down
        board[i][j]= '*'
        # four direction to search
        if j>0:
            self.dfs(board,pNode,i,j-1,res)
        if j<len(board[0])-1:
            self.dfs(board,pNode,i,j+1,res)
        if i>0:
            self.dfs(board,pNode,i-1,j,res) 
        if i<len(board)-1:
            self.dfs(board,pNode,i+1,j,res)
        # move uptown
        board[i][j]=original

    def buildTrie(self,words):
        """
        building the trie node tree ended with 
        the words, in order to check whether has this word
        """
        root=TrieNode()
        for word in words:
            cur=root
            for ch in word:
                pos=ord(ch)-97
                # if not add the node
                if not cur.childlist[pos]:
                    cur.childlist[pos]=TrieNode()
                # move on the next level
                cur=cur.childlist[pos]
            # save the word in last node
            cur.val=word
        return root    
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        row=len(board)
        col=len(board[0])
        # building the tree
        root=self.buildTrie(words)
        for i in xrange(row):
            for j in xrange(col):
                self.dfs(board,root,i,j,res)
        return res
        