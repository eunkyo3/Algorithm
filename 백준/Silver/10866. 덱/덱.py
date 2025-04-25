import sys

class deque:
    def __init__(self):
        self.arr = []
    
    def push_front(self, x):
        self.arr.insert(0, x)

    def push_back(self, x):
        self.arr.append(x)
    
    def pop_front(self):
        print(self.arr.pop(0) if self.arr else -1)

    def pop_back(self):
        print(self.arr.pop() if self.arr else -1)

    def size(self):
        print(len(self.arr))

    def empty(self):
        print(1 if not self.arr else 0)

    def front(self):
        print(self.arr[0] if self.arr else -1)
    
    def back(self):
        print(self.arr[-1] if self.arr else -1)


input = sys.stdin.readline  # 빠른 입력 처리

d = deque()
t = int(input())

for _ in range(t):
    text = input().strip().split()
    command = text[0]

    if command == 'push_front':
        d.push_front(int(text[1]))
    elif command == 'push_back':
        d.push_back(int(text[1]))
    elif command == 'pop_front':
        d.pop_front()
    elif command == 'pop_back':
        d.pop_back()
    elif command == 'size':
        d.size()
    elif command == 'empty':
        d.empty()
    elif command == 'front':
        d.front()
    elif command == 'back':
        d.back()
