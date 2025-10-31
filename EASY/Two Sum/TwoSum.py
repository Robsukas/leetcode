class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        i = 0

        for num in nums:
            needed_num = target - num

            if needed_num in num_dict.keys():
                return [num_dict.get(needed_num), i]

            num_dict[num] = i
            i += 1
        return False
