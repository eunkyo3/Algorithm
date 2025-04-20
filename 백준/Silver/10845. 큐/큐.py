import sys
input = sys.stdin.readline

class Q:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        print(self.arr.pop(0) if self.arr else -1)

    def size(self):
        print(len(self.arr))

    def empty(self):
        print(1 if not self.arr else 0)

    def front(self):
        print(self.arr[0] if self.arr else -1)

    def back(self):
        print(self.arr[-1] if self.arr else -1)

n = int(input())
queue = Q()

for _ in range(n):
    t = input().strip().split()
    op = t[0]

    if op == 'push':
        queue.push(t[1])
    elif op == 'pop':
        queue.pop()
    elif op == 'size':
        queue.size()
    elif op == 'empty':
        queue.empty()
    elif op == 'front':
        queue.front()
    elif op == 'back':
        queue.back()
