# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p is root or q is root:
            return root
        
        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        # If both found something, current root is the LCA
        if left_ancestor and right_ancestor:
            return root
        
        # Otherwise, return whichever side found something (or None if neither did)
        return left_ancestor or right_ancestor