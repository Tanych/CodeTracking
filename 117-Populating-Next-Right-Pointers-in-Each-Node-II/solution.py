# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        newhead=TreeLinkNode(0)
        pre=newhead
        
        while root:
            if root.left:
                pre.next=root.left
                pre=pre.next
            if root.right:
                pre.next=root.right
                pre=pre.next
            # to next nod    
            root=root.next
            
            if not root:
                pre=newhead
                # get new start
                root=pre.next
                newhead.next=None
            