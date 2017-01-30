class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        cnt = 0

        prevLetter = ' '

        for l in s:
            if l != ' ' and prevLetter == ' ':
                cnt += 1

            prevLetter = l

        return cnt
