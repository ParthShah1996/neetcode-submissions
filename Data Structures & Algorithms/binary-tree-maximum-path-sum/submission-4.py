# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def helper(node):
            nonlocal max_sum 

            if not node:
                return 0

            # Get max gain from left and right subtrees. 
            # If a child sum is negative, we ignore it by taking max(0, sum)
            left_gain = max(0, helper(node.left))
            right_gain = max(0, helper(node.right))   

            # Price of the path passing THROUGH this node as the peak
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum
            max_sum = max(max_sum, current_path_sum)
            
            # Return the max gain this node can add to its parent (can only pick ONE branch)
            return node.val + max(left_gain, right_gain) 

        helper(root)

        return max_sum