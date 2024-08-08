class Solution:
    def evalRPN(self, tokens):
        stack = []
        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "-":
                a , b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())                
            elif n == "/":
                a , b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(n))

        return stack[0]