class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(int((2*n)**0.5)-2, int((2*n)**0.5)+1):
            if i*(i+1) <= 2*n < (i+1)*(i+2):
                return i
