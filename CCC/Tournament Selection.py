total = 0

for x in range(6):
    game = input()
    if (game == 'W'):
        total = total + 1
    elif (game != 'W'):
        total = total + 0

if (total >= 5):
    print("1")
elif (total >= 3):
    print("2")
elif (total >= 1):
    print("3")
elif (total == 0):
    print("-1")