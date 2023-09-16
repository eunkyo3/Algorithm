import sys, copy

input = sys.stdin.readline
original = ['a', 'c', 'i', 'j', 'n', 'o', 't', 'w', 'v']
replace = ["@", "[", "!", ";", "^", "0", "7", "\\\\\'", "\\\'"]

for _ in range(int(input())):
    word = str(input().rstrip())
    count = 0
    idx = 0
    while True:
        tmp = word.replace(replace[idx], original[idx], 1)
        if tmp != word:
            word = copy.deepcopy(tmp)
            count += 1
        else:
            idx += 1

        if idx == 9:
            if count >= len(word) / 2:
                print("I don't understand")
            else:
                print(tmp)
            break