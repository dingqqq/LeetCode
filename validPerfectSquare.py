class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        if int(num ** 0.5) ** 2 == num:
            return True
        else:
            return False
