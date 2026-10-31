# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return 1
            left_height = height(root.left)
            right_height = height(root.right)

            return max(left_height, right_height) + 1 
        
        left_height = height(root.left)
        right_height = height(root.right)
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        # print(left_balanced, right_balanced, left_height, right_height)
        if not (left_balanced and right_balanced):
            return False
        if abs(left_height - right_height) > 1:
            return False
        else:
            return True

        