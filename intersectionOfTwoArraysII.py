class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """
        result = []
        for num1 in nums1:
            if num1 in nums2:
                result.append(num1)
                nums2.remove(num1)

        return result
        """

        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)

        result = []
        i = 0
        j = 0
        while i <= len(nums1_sorted) - 1 and j <= len(nums2_sorted) - 1:
            if nums1_sorted[i] == nums2_sorted[j]:
                result.append(nums1_sorted[i])
                i += 1
                j += 1
            elif nums1_sorted[i] < nums2_sorted[j]:
                i += 1
            else:
                j += 1
        return result
        