class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif token[0]=="-" and len(token)>1:
                stack.append(int(token[1:])*-1)

            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == "+":
                    stack.append(operand1+operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "-":
                    stack.append(operand2-operand1)
                elif token=="/":

                    stack.append(int(operand2/operand1))


        return stack[-1]
        