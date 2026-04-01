# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.value = None

        def rec(node):
            if not node or self.value is not None:
                return
            
            rec(node.left)

            self.count += 1
            if self.count == k:
                self.value = node.val
                return

            rec(node.right)

        rec(root)
        return self.value




