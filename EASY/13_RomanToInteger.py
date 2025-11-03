class Solution:
    def romanToInt(self, s: str) -> int:
        list_of_chars = list(s[::-1])
        map_of_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        arabic_num = 0
        last_num = 0

        while len(list_of_chars) > 0:
            num = map_of_nums.get(list_of_chars.pop(0))

            if last_num > num and last_num != 0:
                arabic_num -= num
            else:
                arabic_num += num

            last_num = num

        return arabic_num
            

        

        