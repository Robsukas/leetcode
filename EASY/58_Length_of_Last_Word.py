class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list_of_words = []
        current_word = ""
        for char in s:
            if char != " ":
                current_word += char
            elif char == " " and current_word == "":
                continue
            else:
                list_of_words.append(current_word)
                current_word = ""
        
        if current_word:
            list_of_words.append(current_word)

        return len(list_of_words[-1])
