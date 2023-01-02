class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        l = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                b = l.pop()
                a = l.pop()
                l.append(ops[i](a, b))
            else:
                l.append(int(i))

        return int(l[-1])