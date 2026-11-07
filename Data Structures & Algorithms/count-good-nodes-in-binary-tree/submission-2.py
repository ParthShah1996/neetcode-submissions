# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque

    def goodNodes(self, root):
        if not root:
            return 0
        count = 0
        q = deque([(root, root.val)])
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                count += 1
            new_max = max(max_val, node.val)
            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))
        return count