while True:
    text = input()
    
    if text == '0':
        break
    
    result = True
    for i in range(len(text)//2):
        if text[i] != text[len(text)-1 -i]:
            result = False
    
    print('yes' if result else 'no')