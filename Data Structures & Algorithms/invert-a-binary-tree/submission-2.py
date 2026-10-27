# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:                      # base case
            return None
        left = self.invertTree(root.left)     # the old left child, inverted in place
        right = self.invertTree(root.right)   # the old right child, inverted in place
        root.left = right
        root.right = left
        return root