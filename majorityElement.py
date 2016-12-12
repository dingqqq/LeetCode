class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

            if dict[num] > n/2:
                return num
