# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False

        if root.left is None:
            if root.right is None:
                return root.val == sum
            else:
                return self.hasPathSum(root.right, sum - root.val)
        elif root.right is None:
            return self.hasPathSum(root.left, sum - root.val)
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
