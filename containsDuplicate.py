class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True
