class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __getitem__(self, item):
        curr = self.head
        for i in range(item):
            curr = curr.next
        return curr.data

    def push(self, value):
        new_data = Node(value)
        self.len += 1
        if self.head is None:
            self.head = new_data
            self.head.next = None
            self.head.prev = None
            self.tail = new_data
        else:
            self.tail.next = new_data
            new_data.prev = self.tail
            self.tail = new_data
        return self.head.data

    def pop(self):
        if self.head is None:
            return None
        else:
            self.len -= 1
            if self.head != self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.tail = None

            return self.tail

    def unshift(self, value):
        new_data = Node(value)
        self.len += 1
        if self.head is None:
            self.head = new_data
            self.head.prev = None
            self.head.next = None
            self.tail = new_data
        else:
            self.head.prev = new_data
            new_data.next = self.head
            new_data.prev = None
            self.head = new_data

    def shift(self):
        if self.head is None:
            return None
        else:
            self.len -= 1
            if self.head != self.tail:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.head = None
            return self.head

    def insert(self, index, value):
        new_data = Node(value)
        curr = self.head
        if len(self) <= index:
            self.push(value)
        elif index == 0:
            self.unshift(value)
        else:
            self.len += 1
            for i in range(index):
                curr = curr.next
            new_data.next = curr
            new_data.prev = curr.prev
            curr.prev.next = new_data
            curr.prev = new_data

    def find(self, v):
        curr = self.head
        while curr.data != v:
            if curr is None:
                return None
            curr = curr.next
        return curr

    def get(self, index):
        return self[index]

    def size(self):
        return self.len

    def __len__(self):
        return self.len

    class Iterator:
        def __init__(self, cur_node):
            self.cur_node = cur_node

        def __next__(self):
            if self.cur_node is None:
                raise StopIteration
            val = self.cur_node.data
            self.cur_node = self.cur_node.next
            return val

    def __iter__(self):
        self.Iterator(self.head)

    def print(self):
        for i in range(len(self)-1, -1, -1):
            print(float("{:.1f}".format(self[i])), end=' ')
        print()
        for i in range(len(self)):
            print(float("{:.1f}".format(self[i])), end=' ')


if __name__ == '__main__':
    myList = LinkedList()
    N = int(input())
    if N != 0:
        elements = input().strip().split()
        for el in elements:
            myList.push(int(el))
    M = int(input())

    for i in range(M):
        operations = input().strip().split()
        if operations[0] == "push":
            myList.push(float(operations[1]))
        if operations[0] == "pop":
            myList.pop()
        if operations[0] == 'unshift':
            myList.unshift(float(operations[1]))
        if operations[0] == 'shift':
            myList.shift()
        if operations[0] == 'insert':
            myList.insert(int(operations[1]), float(operations[2]))
    myList.print()