player_hp = 100
RED_POTION = 10
GREEN_POTION = 20
PAPER_CUT = 1000

while True:
    print("what do you want to do")
    desition = input("r. drink red potion g. drink green potion")
    if desition == "r":
        player_hp += RED_POTION
    elif desition == "g":
        player_hp -= GREEN_POTION
    elif desition == "p":
        print ("unofficial closing of the game.")
        exit()
    else:
        print ("not a valid input")
    print(f'players health is now {player_hp}')





