class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        result = []
        carry = 0
        while len(num2) > 0 or len(num1) > 0 or carry == 1:
            last1 = int(num1[-1]) if len(num1) > 0 else 0
            last2 = int(num2[-1]) if len(num2) > 0 else 0

            s = last1 + last2 + carry
            if s <= 9:
                carry = 0
                result.append(str(s))
            else:
                carry = 1
                result.append(str(s - 10))

            num1 = num1[:-1] if len(num1) > 0 else num1
            num2 = num2[:-1] if len(num2) > 0 else num2

        return ''.join(result[::-1])
