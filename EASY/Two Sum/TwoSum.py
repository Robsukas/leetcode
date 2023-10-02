class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = nums[:]
        index1 = 0
        pop_count = 0
        for i in nums:
            nums2.pop(0)
            pop_count += 1
            index2 = 0
            for j in nums2:
                if i + j == target:
                    return [index1, index2 + pop_count]
                index2 += 1
            index1 += 1