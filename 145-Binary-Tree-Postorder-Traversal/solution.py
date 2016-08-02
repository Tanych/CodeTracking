# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # using stack ways
        stck=[]
        # current node
        cur=root
        peak=last=None
        res=[]
        while cur or stck:
            if cur:
                stck.append(cur)
                cur=cur.left
            elif stck:
                # get the peak
                peak=stck[-1]
                # if has right branch, we need get right first
                # mark the peak and add the right subtree to stack
                # if subtree has all print out, add the peak val
                # last!=peak.right, aviod revisited
                if peak.right and last!=peak.right:
                    cur=peak.right
                # no right branch, directly add to res
                else:
                    res.append(peak.val)
                    last=peak
                    stck.pop()
        return res
                