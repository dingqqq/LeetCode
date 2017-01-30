# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def symmetricNodes(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is not None and rightNode is not None:
            return (leftNode.val == rightNode.val) and self.symmetricNodes(leftNode.left, rightNode.right) and self.symmetricNodes(leftNode.right, rightNode.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        elif root.left is not None and root.right is not None:
            return (root.left.val == root.right.val) and self.symmetricNodes(root.left, root.right)
        else:
            return False
