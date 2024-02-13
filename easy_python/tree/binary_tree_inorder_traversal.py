# then add everything tgt

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

"""We can use a helper function and pass in an empty list into it so taht we can just add into it"""