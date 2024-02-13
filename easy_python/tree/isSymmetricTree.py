class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left_sub = root.left
        right_sub = root.right
        return self.isMirror(left_sub, right_sub)

    def isMirror(self, left_sub, right_sub):
        if left_sub == None and right_sub == None:
            return True
        elif left_sub == None or right_sub == None:
            return False
        else:
            return left_sub.val == right_sub.val and self.isMirror(left_sub.left, right_sub.right) and self.isMirror(
                left_sub.right, right_sub.left)