class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        if len(nums) == 1:
            return 0

        moves = 0
        while max(nums) != min(nums):
            max_num = max(nums)
            max_index = nums.index(max_num)

            nums_copy = nums[:]
            del nums_copy[max_index]
            max2_num = max(nums_copy)

            if max_num - max2_num > 1:
                for i in range(len(nums)):
                    if i != max_index:
                        nums[i] += (max_num - max2_num)
                moves += (max_num - max2_num)
            else:
                for i in range(len(nums)):
                    if i != max_index:
                        nums[i] += 1
                moves += 1

        return moves
        """

        return sum(nums) - len(nums) * min(nums)