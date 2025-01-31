n = int(input())  
i = 1  
layer = 1  

while n > layer:  
    layer += 6 * i  
    i += 1

print(i)
