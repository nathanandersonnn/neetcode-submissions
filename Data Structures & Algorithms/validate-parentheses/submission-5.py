class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}' : '{'}
        for char in s:
            if char in matches:
                if not stack or stack.pop() != matches[char]:
                    return False
            else:
                stack.append(char)
        return not stack