내소리 = input()
병원 = input()

my_sound = 0
hos_sound = 0

for i in range(len(내소리)):
    if 내소리[i] == 'a':
        my_sound += 1

for i in range(len(병원)):
    if 병원[i] == 'a':
        hos_sound += 1

if my_sound >= hos_sound:
    print('go')
else:
    print('no')