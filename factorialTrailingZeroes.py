class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        tmp = n/5
        result = 0
        while tmp > 0:
            result += tmp
            tmp /= 5

        return result
