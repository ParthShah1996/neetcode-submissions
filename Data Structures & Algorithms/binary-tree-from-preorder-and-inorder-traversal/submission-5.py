# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_bound, right_bound):
            nonlocal pre_idx
            if left_bound > right_bound:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_index_map[root_val]
            root.left = helper(left_bound, mid - 1)
            root.right = helper(mid + 1, right_bound)
            return root

        return helper(0, len(inorder) - 1)