import math

A, B, V = map(int, input().split())
k = (V-B) / (A-B)
print(math.ceil(k))