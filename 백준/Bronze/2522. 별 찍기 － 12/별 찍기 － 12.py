'''

예제 입력 1 
3
예제 출력 1 
  *
 **
***
 **
  *

'''

n = int(input())
for i in range(n-1, -1, -1):
    print(' '*i+'*'*(n-i))
for i in range(n-1, 0, -1):
    print(' '*(n-i)+'*'*i)