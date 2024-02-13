class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    """Max depth goes to very bottom first , then reverse once and goes right"""
    """Everytime it reverses backup, it adds one. So at the end, max of one path is obtained."""

