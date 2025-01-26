t = int(input())

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

for _ in range(t):
    c = int(input())
    res = []
    
    res.append(c // Quarter)
    c = c % Quarter
    res.append(c // Dime)
    c = c % Dime
    res.append(c // Nickel)
    c = c % Nickel
    res.append(c // Penny)
    c = c % Penny

    print(*res)