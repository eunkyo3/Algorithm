n = int(input())

for _ in range(n):
    ps = input()
    stack = []
    is_vps = True

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()  
            else:
                is_vps = False
                break

    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
