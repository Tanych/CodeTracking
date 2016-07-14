# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        # using hash map to store the value of the object
        hashmap={}
        hashmap[head]=RandomListNode(head.label)
        p=head
        while p:
            if p.random:
                # if the first time to create, build the node
                if p.random not in hashmap:
                    hashmap[p.random]=RandomListNode(p.random.label)
                # if already create, directy pointer
                hashmap[p].random=hashmap[p.random]
            if p.next:
                # if the first time to create, build the node
                if p.next not in hashmap:
                    hashmap[p.next]=RandomListNode(p.next.label)
                # if already create, directy pointer
                hashmap[p].next=hashmap[p.next]
            # move on
            p=p.next
        return hashmap[head]
        