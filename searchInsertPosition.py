class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        leftBound = 0
        rightBound = len(nums) - 1

        while leftBound < rightBound:
            curLoc = (leftBound + rightBound) / 2
            if nums[curLoc] == target:
                return curLoc
            elif nums[curLoc] > target:
                rightBound = curLoc - 1
            else:
                leftBound = curLoc + 1

        if nums[leftBound] < target:
            return leftBound + 1
        else:
            return leftBound
