import sys
from collections import deque

arr = deque()
input = sys.stdin.readline

def push(x):
    arr.append(x)

def pop():
    if not arr:
        print(-1)
    else:
        print(arr.popleft())

def size():
    print(len(arr))

def empty():
    print(1 if not arr else 0)

def front():
    if not arr:
        print(-1)
    else:
        print(arr[0])

def back():
    if not arr:
        print(-1)
    else:
        print(arr[-1])

n = int(input())

for _ in range(n):
    parts = input().split()
    op = parts[0]

    match op:
        case 'push':
            push(parts[1])
        case 'pop':
            pop()
        case 'size':
            size()
        case 'empty':
            empty()
        case 'front':
            front()
        case 'back':
            back()
