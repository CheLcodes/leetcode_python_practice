class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in '+-*/':
                if len(stack) < 2:
                    raise Exception('Invalid input!')
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    if b == 0:
                        raise Exception('Invalid division!')
                    res = int(a / b)
                stack.append(res)
            elif token.isdigit():
                stack.append(int(token))
            else:
                raise Exception('Invalid character!')
        if len(stack) != 1:
            raise Exception('Invalid input!')
        return stack.pop()


sol = Solution()
res = sol.evalRPN(["4","13","0","/","+"])
print('This is the answer', res)