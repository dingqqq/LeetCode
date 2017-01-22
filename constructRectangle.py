class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        result = [area, 1]
        for i in range(1, int(area**0.5+1)):
            if area % i == 0:
                result = [area/i, i]

        return result
