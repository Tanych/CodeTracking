# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        res=[]
        queue=collections.deque([])
        queue.append(root)
        while queue:
            node=queue.popleft()
            if not node:
                res.append('#')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        # save the node
        queue=collections.deque([])
        treenodes=data.split()
        root=TreeNode(int(treenodes[0]))
        queue.append(root)
        
        i=1
        while i<len(treenodes):
            parent=queue.popleft()
            if treenodes[i]!='#':
                left=TreeNode(int(treenodes[i]))
                parent.left=left
                queue.append(left)
            i+=1
            if  treenodes[i]!='#':
                right=TreeNode(int(treenodes[i]))
                parent.right=right
                queue.append(right)
            i+=1
        
        return root
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))