class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        resultDict = {1: 1, 2: 2}
        for i in range(3, n+1):
            result = resultDict[i - 1] + resultDict[i - 2]
            resultDict[i] = result

        return result