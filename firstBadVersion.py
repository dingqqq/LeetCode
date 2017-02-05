# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isBadVersion(1):
            return 1

        left = 1
        right = n
        mid = (left + right) / 2

        while right - left >= 2:
            if isBadVersion(mid):
                right = mid
                mid = (left + right) / 2
            else:
                left = mid
                mid = (left + right) / 2

        return right

