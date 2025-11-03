class Solution:
    def isValid(self, s: str) -> bool:
        list_of_parentheses = list(s)
        opened_stack = []
        opening_parentheses = ["(", "[", "{"]
        legal_closing_dict = {"(": ")", "[": "]", "{": "}"}

        for i in list_of_parentheses:
            if opened_stack != []:
                if i in opening_parentheses:
                    opened_stack.append(i)
                else:
                    if i == legal_closing_dict.get(opened_stack.pop()):
                        continue
                    else:
                        return False
            else:
                opened_stack.append(i)
        
        return opened_stack == []