# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None:
            if root.right is None:
                return [str(root.val)]
            else:
                return [str(root.val) + "->" + x for x in self.binaryTreePaths(root.right)]
        else:
            if root.right is None:
                return [str(root.val) + "->" + x for x in self.binaryTreePaths(root.left)]
            else:
                return [str(root.val) + "->" + x for x in self.binaryTreePaths(root.left)] + [str(root.val) + "->" + x for x in self.binaryTreePaths(root.right)]