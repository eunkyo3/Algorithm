input_str = input()
new_str = ""

for i in range(len(input_str)):
    if input_str[i].islower():
        new_str += input_str[i].upper()
    else:
        new_str += input_str[i].lower()

print(new_str)
