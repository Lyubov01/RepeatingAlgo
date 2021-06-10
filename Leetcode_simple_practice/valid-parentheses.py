class Solution:
    
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        class Stack:
            def __init__(self):
                self.items = []

            def push(self, el):
                self.items.insert(0, el)
                return el

            def is_empty(self):
                if self.items:
                    return False
                return True

            def pop(self):
                if not self.is_empty():
                    r = self.items[0]
                    self.items.remove(r)
                    return r
                return None

            def reverse(self):
                revers = []
                for i in range(len(self.items)):
                    revers.append(self.items[len(self.items) - i - 1])
                self.items = revers

            def peek(self):
                try:
                    return self.items[0]
                except IndexError:
                    return None

        d = {')': '(', '}': '{', ']': '['}

        stack = Stack()
        for sym in s:
            if sym in d.values():
                stack.push(sym)

            elif d[sym] == stack.peek():
                stack.pop()
            else:
                return False
        return stack.is_empty()








