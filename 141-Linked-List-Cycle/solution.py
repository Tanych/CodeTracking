# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        p=head
        hashmap={}
        
        while p:
            if p in hashmap:
                return True
            else:
                hashmap[p]=hashmap.get(p,0)+1
            p=p.next
            
        return False