word = input()
isPalindrome = True
result = 0

for i in range(len(word) // 2):
    if word[i] != word[len(word) -1 -i]:
        isPalindrome = False
        break

if isPalindrome:
    result = 1

print(result)