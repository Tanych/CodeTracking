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
        def helper(root):
            if root:
                res.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                res.append('#')
        res=[]
        helper(root)
        # using the space ' ' to sperate in order to get iteration
        return ' '.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val=next(iter_nodes)
            if val=='#':
                return None
            root=TreeNode(int(val))
            root.left=helper()
            root.right=helper()
            return root
        iter_nodes=iter(data.split())
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))