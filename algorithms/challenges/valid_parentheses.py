# source: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "]": "[", "}": "{"}
        stack = []

        for el in s:
            if len(stack) > 0:
                if el in closing and stack[-1] == closing[el]:
                    stack.pop()
                    continue
                else:
                    stack.append(el)
                    continue
            stack.append(el)

        if len(stack) == 0:
            return True
        else:
            return False    
                    