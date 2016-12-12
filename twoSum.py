class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            dict[target - nums[i]] = i

        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
