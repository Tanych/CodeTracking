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
        
    def getKitem(self,k):
        cur=self.head
        i,res=0,[0]*k
        while cur and i<k:
            res[i]=cur.val
            cur=cur.next
            i+=1
        
        while cur:
            # select j from 0-i
            j=random.randint(0, i)
            # if the pick index less than k, replace it
            if j<k:
                res[j]=cur.val
            cur=cur.next
            i+=1
        return res
    
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res=self.head.val
        node=self.head.next
        i=2
        while node:
            j=random.randint(0, i-1)
            if j<1:
                res=node.val
            i+=1
            node=node.next
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()