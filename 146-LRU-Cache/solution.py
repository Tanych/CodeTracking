class DoubleLinkedNode(object):
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.pre=None
        self.next=None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head=None
        self.tail=None
        self.hashmap={}
        self.size=0
        self.maxsize=capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hashmap:
            node=self.hashmap[key]
            val=node.val
            self.delete(node)
            self.insert(node)
            return val
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hashmap:
            node=self.hashmap[key]
            node.val=value
            self.delete(node)
            self.insert(node)
        else:
            self.insert(DoubleLinkedNode(key,value))
        
    def insert(self,node):
        if self.size==self.maxsize:
             self.delete(self.tail)
        if not self.head:
             self.head=node
             self.tail=node
        else:
            self.head.pre=node
            node.next=self.head
            self.head=node
        # keep in mind
        self.hashmap[node.key]=node
        self.size+=1
        
    def delete(self,node):
        if node==self.head:
            self.head=node.next
        if node==self.tail:
            self.tail=node.pre
        if node.pre:
            node.pre.next=node.next
        if node.next:
            node.next.pre=node.pre
        # don't forget to do so
        node.pre=None
        node.next=None
        del self.hashmap[node.key]
        self.size-=1
        