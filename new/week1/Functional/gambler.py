import random

stake = int(10)
goal = int(10)
trail = int(10)
bet = 0
win = 0

for i in range(trail):
    cash = stake
    if 0 < cash < goal:
        bet += 1
        if random.randint(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        print("congrats")

print(str(100 * (win // trail) + int('wins')))
print('Avg # bets: ' + str(bet // trail))
