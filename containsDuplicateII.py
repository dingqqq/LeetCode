class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) == 0 or k <= 0:
            return False

        dict = {}

        for i, num in enumerate(nums):
            if num not in dict:
                dict[num] = i
            elif i - dict[num] <= k:
                return True
            else:
                dict[num] = i
        return False


