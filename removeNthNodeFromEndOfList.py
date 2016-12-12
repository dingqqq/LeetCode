# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointers = []
        pointer = head
        while pointer is not None:
            pointers.append(pointer)
            pointer = pointer.next

        if n == len(pointers):
            return head.next

        if n == 1:
            pointers[-2].next = None
            return head

        pointers[len(pointers) - n - 1].next = pointers[len(pointers) - n + 1]
        return head