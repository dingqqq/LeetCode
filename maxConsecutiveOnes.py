class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxConsecutiveOnes = 0
        currentConsecutiveOnes = 0
        for i in nums:
            if i == 1:
                currentConsecutiveOnes += 1
            else:
                maxConsecutiveOnes = max(maxConsecutiveOnes, currentConsecutiveOnes)
                currentConsecutiveOnes = 0

        maxConsecutiveOnes = max(maxConsecutiveOnes, currentConsecutiveOnes)
        return maxConsecutiveOnes
