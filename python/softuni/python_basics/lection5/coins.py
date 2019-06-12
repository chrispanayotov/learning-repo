change = float(input())
change_int = int(change * 100)

coins = 0

while change_int > 0:
    while change_int >= 100:
        if change_int >= 200:
            change_int -= 200
            coins += 1
        elif change_int >= 100 and change_int < 200:
            change_int -= 100
            coins += 1

    if change_int >= 50:
        change_int -= 50
        coins += 1
    while change_int >= 20:
        change_int -= 20
        coins += 1
    if 9 < change_int < 20:
        change_int -= 10
        coins +=1    
     
    if change_int >= 5:
        change_int -= 5
        coins += 1
    elif 1 < change_int < 5:
        change_int -= 2
        coins += 1
    elif change_int == 1:
        change_int -= 1
        coins += 1

print(coins)