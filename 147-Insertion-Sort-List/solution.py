# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        # -1->head
        thead=ListNode(-1)
        thead.next=head
        pre=thead
        cur=head
        # search every elements in head
        while cur:
            if cur.next and cur.next.val<cur.val:
                # for in previous larger than cur.next
                while pre.next and pre.next.val<cur.next.val:
                    pre=pre.next
                # found the correct position, combine
                # -1-1-2(pre)-5(cur)-3(cur.next)-6
                # 1--record the next positon
                tnode=pre.next
                # 2->3 break 2->5
                pre.next=cur.next
                # 5->6 break 5->3
                cur.next=cur.next.next
                # rebuild 3->5
                pre.next.next=tnode
                # the sorted would be -1-1-2-3-5-6
                # move back pre to start
                pre=thead
            
            else:
                cur=cur.next
            
        return thead.next
        
                