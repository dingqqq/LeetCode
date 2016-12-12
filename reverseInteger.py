class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        if x < 0:
            return -self.reverse(-x)

        y = int(str(x)[::-1])

        if y > 2**31 - 1:
            return 0
        else:
            return y