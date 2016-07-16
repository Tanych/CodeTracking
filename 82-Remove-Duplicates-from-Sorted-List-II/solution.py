# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        newhead=ListNode(-2<<31-1)
        prepre=newhead
        newhead.next=head
        pre=head
        cur=head.next
        
        while cur:
            if pre.val==cur.val:
                while cur and pre.val==cur.val:
                    cur=cur.next
                if not cur:
                    prepre.next=None
                    break
                else:
                    p=cur.next
                    prepre.next=cur
                    pre=cur
                    cur=p
            else:
                prepre=pre
                pre=cur
                cur=cur.next
                
        return newhead.next
        