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
            root=root.next
            # if root reaches the right most
            # go to the next level
            if not root:
                # reset pre to the new head
                pre=newhead
                # get the next level left most head 
                root=newhead.next
                # make the last level link broken
                # if works well only for the last level
                # since if root.left or root.right is not none
                # the pre.next will change the value
        newhead.next=None
        