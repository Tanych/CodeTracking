# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        # using two pointer to access the linked list
        # fast speed is 2 times of slow
        # suppose the meet at c, the start is a, 
        # cycle start is b
        # a->b=x, b->c=y c->a=z
        # 2(x+y)=x+y+z+y====> x==z 
        # the step slow move is equal fast move from
        # meet point to the cycle start point
        
        slow=head
        fast=head
        hascycle=False
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                hascycle=True
                break
        if not hascycle:
            return None
        
        # check slow from head,
        # steps move equal fast move from meeting point
        
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
            
        return slow
        
                