class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        numSet = set()

        while n not in numSet:
            numSet.add(n)
            digits = list(str(n))
            n = 0
            for digit in digits:
                n += int(digit) ** 2

            if n == 1:
                return True

        return False