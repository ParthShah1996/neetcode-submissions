# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def ifAncestor(self, root: TreeNode, node:TreeNode):
        if not root:
            return None
        
        if root == node:
            return True
        
        else:
            return self.ifAncestor(root.right, node) or self.ifAncestor(root.left, node)
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.ifAncestor(root.right, p) and self.ifAncestor(root.right, q):
            node = root.right
            return self.lowestCommonAncestor(node, p, q)
        elif self.ifAncestor(root.left, p) and self.ifAncestor(root.left, q):
            node = root.left
            return self.lowestCommonAncestor(node, p, q)
        else:
            return root
            
        

        
    
        
