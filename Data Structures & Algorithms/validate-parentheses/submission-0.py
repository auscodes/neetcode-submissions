class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')' : '(', ']' :  '[', '}' : '{'}

        for c in s:
            if c in mp: # close bracket
                if stack and stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False
            else: # open bracket
                stack.append(c)

        return True if not stack else False
    