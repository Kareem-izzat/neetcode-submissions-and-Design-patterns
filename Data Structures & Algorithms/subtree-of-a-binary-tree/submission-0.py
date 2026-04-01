# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1:
            return False
        if self.same(root1,root2):
            return True
        return self.isSubtree(root1.left,root2) or self.isSubtree(root1.right,root2)
        


    def same(self,root1,root2):
        if not root1 and root2:
            return False
        if root1 and  not root2:
            return False
        if not root1 and not root2:
            return True

        return root1.val == root2.val and self.same(root1.left ,root2.left) and self.same(root1.right,root2.right)