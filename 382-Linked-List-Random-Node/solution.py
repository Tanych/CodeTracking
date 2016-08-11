# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n=0
        node=self.head
        while node:
            node=node.next
            n+=1
        node=self.head
        for i in xrange(random.randrange(n)):
            node=node.next
        return node.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()