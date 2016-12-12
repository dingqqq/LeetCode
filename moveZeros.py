class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            pass
        else:
            j = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
