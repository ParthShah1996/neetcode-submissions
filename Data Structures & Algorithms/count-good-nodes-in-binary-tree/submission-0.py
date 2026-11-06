# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            # Base case: if node is None, it adds 0 to our count
            if not node:
                return 0
            
            # Check if the current node is "good"
            count = 1 if node.val >= max_val else 0
            
            # Update the max value seen so far along this path
            new_max = max(max_val, node.val)
            
            # Recurse down to left and right children, passing the new max
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        # Start the recursion from the root, initializing max_val 
        # with the root's own value (or negative infinity / smallest possible int)
        return dfs(root, root.val)