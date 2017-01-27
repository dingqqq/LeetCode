class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        while len(s) > 0 and s[-1] == ' ':
            s = s[:-1]

        if len(s) == 0:
            return 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == ' ':
                return len(s) - i - 1

        return len(s)
