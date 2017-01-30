class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'

        prevResult = self.countAndSay(n-1)

        curResult = ''
        prevNum = None
        cnt = 0

        for curNum in prevResult:
            if prevNum is None:
                prevNum = curNum
                cnt = 1
            elif curNum == prevNum:
                cnt += 1
            else:
                curResult += str(cnt) + str(prevNum)
                prevNum = curNum
                cnt = 1

        curResult += str(cnt) + str(prevNum)
        return curResult
