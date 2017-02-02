# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        firstNode = ListNode(0)
        firstNode.next = head

        prevNode = firstNode
        curNode = head

        while curNode is not None:
            if curNode.val == val:
                curNode = curNode.next
                prevNode.next = curNode
            else:
                prevNode = curNode
                curNode = curNode.next

        return firstNode.next
