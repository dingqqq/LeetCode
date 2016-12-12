class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        """
        if n <= 3:
            return True

        wins = set([1,2,3])

        for i in xrange(4, n+1):
            for win in wins:
                if i - win not in wins:
                    wins.add(i)
                    break

        if n in wins:
            return True
        else:
            return False
        """

        return not n % 4 == 0