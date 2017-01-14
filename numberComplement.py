class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        return num ^ int('1' * (len(bin(num))-2), 2)