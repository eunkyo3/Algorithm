text = list(input())
boomb_str = list(input())

stack = []

for i in text:
    stack.append(i)
    if stack[-len(boomb_str)::] == boomb_str:
        del stack[-len(boomb_str)::]

if stack:
    print(*stack, sep='')
else:
    print('FRULA')