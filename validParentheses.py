class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if (last == '(' and c == ')') or (last == '[' and c == ']') or (last == '{' and c == '}'):
                    pass
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
