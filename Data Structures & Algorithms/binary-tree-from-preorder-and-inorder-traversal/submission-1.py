# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map to lookup value indices in inorder array in O(1) time
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        preorder_iter = iter(preorder)
        def helper(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            
            # The next value in preorder is the current root
            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            # Split the inorder array into left and right subtrees
            mid = inorder_index_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = helper(left_bound, mid - 1)
            root.right = helper(mid + 1, right_bound)
            
            return root

        return helper(0, len(inorder) - 1)