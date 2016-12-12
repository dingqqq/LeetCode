class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        result = nums[0]
        for num in nums[1:]:
            result ^= num

        return result
