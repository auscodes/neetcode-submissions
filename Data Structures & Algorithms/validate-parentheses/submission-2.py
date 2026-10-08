class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in mp: # close bracket
                if stack and stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False

            else: # open
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
