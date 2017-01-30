class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = []
        prevRow = []
        for i in range(1, numRows+1):
            if i == 1:
                currentRow = [1]
            else:
                currentRow = [prevRow[0]] + [prevRow[j] + prevRow[j+1] for j in range(i-2)] + [prevRow[-1]]

            result.append(currentRow)
            prevRow = currentRow

        return result
