class Solution:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        interval = [-99999, 99999]

        def rec(node, interval):
            if not node:
                return True

            # Check current node is within valid range
            if not (interval[0] < node.val < interval[1]):
                return False

            # Correct intervals:
            leftInterval = [interval[0], node.val]
            rightInterval = [node.val, interval[1]]

            return rec(node.left, leftInterval) and rec(node.right, rightInterval)

        return rec(root, interval)