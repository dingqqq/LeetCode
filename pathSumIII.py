# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root, sum):
        if root is None:
            return 0

        if root.val == sum:
            return 1 + self.traverse(root.left, sum-root.val) + self.traverse(root.right, sum-root.val)
        else:
            return self.traverse(root.left, sum-root.val) + self.traverse(root.right, sum-root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if root is None:
            return 0

        return self.traverse(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
