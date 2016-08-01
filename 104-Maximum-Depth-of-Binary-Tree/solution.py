# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs search
        if not root:
            return 0
        
        #return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
        
        # the recursive method is very straightforward
        # in real or interview, need to implement using stack and some advanced traval tech
        # not level by level
        """
        ### simple bfs

        stck=[root]
        depth=0
        # bfs search
        while stck:
            tmp=[]
            depth+=1
            for cur in stck:
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            stck=tmp
        return depth
        """
        
        ### implement not level by level
        stck=[root]
        depth=0
        # record the previous route
        prenode=None
        
        while stck:
            cur=stck[-1]
            #  if prenode is above cur node
            if not prenode or prenode.left==cur or prenode.right==cur:
                # left has priority to add, if--elif not if---if 
                if cur.left:
                    stck.append(cur.left)
                elif cur.right:
                    stck.append(cur.right)
            
            # else if the travel back from bottom, the left subtree is completed
            elif cur.left==prenode:
                if cur.right:
                    stck.append(cur.right)
            # reach the leaf node, prenode and cur reach the same node
            else:
                stck.pop()
                
            # move pre to next route     
            prenode=cur
            depth=max(depth,len(stck))
            
        return depth
        