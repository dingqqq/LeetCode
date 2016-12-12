class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) == 0:
            return t

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return t_sorted[i]

        return t_sorted[-1]
