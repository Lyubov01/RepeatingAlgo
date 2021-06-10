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
            revers.append(self.items[len(self.items)-i-1])
        self.items = revers

    def repr(self):
        for item in self.items:
            print(float(item), end=' ')


if __name__ == '__main__':
    stack = Stack()
    M = int(input())

    for i in range(M):
        command = input().strip().split()
        if command[0] == 'push':
            stack.push(command[1])
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'reverse':
            stack.reverse()
    stack.repr()
