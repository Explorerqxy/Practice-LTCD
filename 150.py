
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        if not tokens:
            return 0
        for  c in tokens:
            if c in ('+','-','*','/'):
                num=int(stack.pop())
                if c=='+':
                    stack[-1]+=num
                elif c=='-':
                    stack[-1]-=num
                if c=='*':
                    stack[-1]*=num
                if c=='/':
                    stack[-1]=int(stack[-1]/num)
            else:
                stack.append(int(c))
        return stack[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t, f = tokens.pop(), self.evalRPN
        if t in '+-*/':
            b, a = f(tokens), f(tokens)
            t = eval('a' + t + 'b')
        return int(t)