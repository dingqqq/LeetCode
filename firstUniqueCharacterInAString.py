class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {}

        for l in s:
            if l not in dict:
                dict[l] = 1
            else:
                dict[l] += 1

        for i, l in enumerate(s):
            if dict[l] == 1:
                return i

        return -1
