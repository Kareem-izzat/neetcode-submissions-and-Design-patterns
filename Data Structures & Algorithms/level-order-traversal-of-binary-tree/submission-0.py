# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_depth(self, root: Optional['TreeNode']) -> int:
        """
        Returns the depth (height) of a binary tree.
        Depth = number of nodes along the longest path from root to leaf.
        """
        if not root:
            return 0  # empty tree has depth 0
        left_depth = self.tree_depth(root.left)
        right_depth = self.tree_depth(root.right)
        return 1 + max(left_depth, right_depth)
    
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        
        length = self.tree_depth(root)
        res = [[] for _ in range(length)]
        
        def rec(node: Optional['TreeNode'], i: int):
            if not node or i >= length:
                return
            res[i].append(node.val)
            rec(node.left, i + 1)
            rec(node.right, i + 1)
        
        rec(root, 0)
        return res