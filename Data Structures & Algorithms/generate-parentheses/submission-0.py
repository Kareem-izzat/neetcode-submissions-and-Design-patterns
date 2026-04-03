class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isPartiallyvalid( s: str) -> bool:
            stack = []


            closeToOpen = {")": "(", "]": "[", "}": "{"}
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
            return True
        parenthesis = []
        length = 1
        start="("
        openning=1
        closing=0
        def rec(start,length,openning,closing):
            if length == n*2:
                parenthesis.append(start)
                return
            option1=start+")"
            option2=start+"("
            #openning=openning+1
            if openning+1<=n and isPartiallyvalid(option2):
                rec(option2,length+1,openning+1,closing)
            #closing = closing + 1
            if closing+1<=n and isPartiallyvalid(option1):
                rec(option1,length+1,openning,closing+1)

        rec(start,length,openning,closing)
        return parenthesis
        