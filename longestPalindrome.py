class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {}

        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1

        result = 0
        is_odd = 0

        for letter in dict:
            if dict[letter] > 1:
                if dict[letter] % 2 == 1:
                    result += dict[letter] - 1
                    is_odd = 1
                else:
                    result += dict[letter]
            else:
                is_odd = 1

        return result + is_odd
