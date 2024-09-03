import sys
input = sys.stdin.readline
print = sys.stdout.write

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return -1
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1
        
    def is_empty(self):
        if len(self.stack) == 0:
            return 1 
        else:
            return 0
    
    def size(self):
        return len(self.stack)

stack = Stack()
test_case = int(input())
for _ in range(test_case):
    num = input().split()

    if num[0] == "1":
        stack.push(num[1])
    elif num[0] == "2":
        print(str(stack.pop()) + "\n")
    elif num[0] == "3":
        print(str(stack.size()) + "\n")
    elif num[0] == "4":
        print(str(stack.is_empty()) + "\n")
    elif num[0] == "5":
        print(str(stack.peek()) + "\n")
    else:
        print('error\n')