# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def partionlist(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        fast=slow.next
        slow.next=None
        return fast
            
        
    def divide(self,head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        midnode=self.partionlist(head)
        root=TreeNode(midnode.val)
        print midnode.val
        left=self.divide(head)
        right=self.divide(midnode.next)
       
        root.left=left
        root.right=right
        return root
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow=head
        fast=head.next
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        root=TreeNode(slow.next.val)    
        rhead=slow.next.next
        slow.next=None
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(rhead)
        return root
        #return self.divide(head)
        