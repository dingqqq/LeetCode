class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """

        if len(str) == 0:
            return False

        for i in range(1, len(str)/2 + 1):
            if len(str) % i == 0:
                if str[:i] * (len(str)/i) == str:
                    return True

        return False
