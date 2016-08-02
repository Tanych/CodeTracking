# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stck,res=[],[]
        cur=root
        while cur or stck:
            if cur:
                stck.append(cur)
                cur=cur.left
            # after all the left node haved added
            elif stck:
                # get the leftmost value
                res.append(stck[-1].val)
                # go to right
                cur=stck[-1].right
                stck.pop()
                
        return res
                