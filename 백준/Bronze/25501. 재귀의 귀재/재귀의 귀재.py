cnt = 0

def recursion(s, l, r):
    global cnt
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())

for _ in range(n):
    text = input()
    cnt = 0
    print(isPalindrome(text), cnt)