# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        queue = [root]
        while len(queue) > 0:
            parentNode = queue.pop(0)
            parentNode.left, parentNode.right = parentNode.right, parentNode.left

            if parentNode.left is not None:
                queue.append(parentNode.left)

            if parentNode.right is not None:
                queue.append(parentNode.right)

        return root
