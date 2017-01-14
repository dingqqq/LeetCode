class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z = x ^ y
        result = 0

        while z > 1:
            result += z % 2
            z /= 2

        result += z

        return result
