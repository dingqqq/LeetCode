class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        first = None
        second = None
        third = None

        for num in nums:
            if first is None:
                first = num
            elif second is None:
                if num > first:
                    second = first
                    first = num
                elif num < first:
                    second = num
            elif third is None:
                if num > first:
                    third = second
                    second = first
                    first = num
                elif second < num < first:
                    third = second
                    second = num
                elif num < second:
                    third = num
            else:
                if num > first:
                    third = second
                    second = first
                    first = num
                elif second < num < first:
                    third = second
                    second = num
                elif third < num < second:
                    third = num

        if third is None:
            return first
        else:
            return third
