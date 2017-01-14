class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_set = set(nums)

        result = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)

        return result

