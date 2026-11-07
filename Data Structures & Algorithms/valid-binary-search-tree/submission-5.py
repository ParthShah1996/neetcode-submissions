# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        def check(node):
            if not node:
                return True, float('inf'), float('-inf')
            lv, lmin, lmax = check(node.left)
            rv, rmin, rmax = check(node.right)
            if not (lv and rv and lmax < node.val < rmin):
                return False, 0, 0
            return True, min(lmin, node.val), max(rmax, node.val)
        return check(root)[0]