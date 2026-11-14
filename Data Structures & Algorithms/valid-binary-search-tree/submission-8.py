# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            
            # Current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Left child must be less than node.val (so high becomes node.val)
            # Right child must be greater than node.val (so low becomes node.val)
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))