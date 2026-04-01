class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)%2 != 0:
            return False
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for bracket in s:
            if bracket in closeToOpen.values():
                stack.append(bracket)
            if bracket in closeToOpen.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
        if len(stack)!= 0:
            return False
        return True