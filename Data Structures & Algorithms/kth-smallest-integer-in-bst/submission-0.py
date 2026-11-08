# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def inorder(node):
            nonlocal counter
            if not node:
                return None
            
            # Check left subtree; if we found the answer, bubble it straight up!
            left = inorder(node.left)
            if left is not None:
                return left
            
            # Process current node
            counter += 1
            if counter == k:
                return node.val
            
            # Check right subtree
            return inorder(node.right)
            
        return inorder(root)