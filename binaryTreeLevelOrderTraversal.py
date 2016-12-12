# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def nodesToList(self, nodes):
        return [node.val for node in nodes if node is not None]

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        result = [[root.val]]

        next_nodes = []
        if root.left is not None:
            next_nodes.append(root.left)
        if root.right is not None:
            next_nodes.append(root.right)

        while len(next_nodes) > 0:
            result.append(self.nodesToList(next_nodes))
            next_nodes_temp = []
            for node in next_nodes:
                if node.left is not None:
                    next_nodes_temp.append(node.left)
                if node.right is not None:
                    next_nodes_temp.append(node.right)
            next_nodes = next_nodes_temp

        return result