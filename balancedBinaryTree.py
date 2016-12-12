# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    ''' Not the fastest solution
    def depth(self, root):
        if root is None:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    '''

    def isBalanced(self, root):
        if root is None:
            return True

        def depth(node):
            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if abs(left_depth - right_depth) > 1:
                raise Exception
            else:
                return max(left_depth, right_depth) + 1
        try:
            return depth(root) > 0
        except:
            return False
        