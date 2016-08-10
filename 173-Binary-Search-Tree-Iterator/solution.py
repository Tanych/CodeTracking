# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder_stack=[]
        self.cur=root
        self.pointer=None

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cur or self.inorder_stack:
            if self.cur:
                self.inorder_stack.append(self.cur)
                self.cur=self.cur.left
            elif self.inorder_stack:
                self.pointer=self.inorder_stack[-1]
                self.cur=self.inorder_stack[-1].right
                self.inorder_stack.pop()
                return True
        return False

    def next(self):
        """
        :rtype: int
        """
        return self.pointer.val
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())