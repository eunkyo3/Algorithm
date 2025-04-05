n, jimin, hansu = map(int, input().split())

players = [i + 1 for i in range(n)]
round = 1

while len(players) > 1:
    next_round = []

    for i in range(0, len(players), 2):
        pair = players[i:i+2]

        if jimin in pair and hansu in pair:
            print(round)
            exit()

        if jimin in pair:
            next_round.append(jimin)
        elif hansu in pair:
            next_round.append(hansu)
        else:
            next_round.append(pair[0])

    players = next_round
    round += 1

print(-1)