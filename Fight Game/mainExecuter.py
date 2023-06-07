#here are executed the leves 
import time
from playerAtributes import player1, player2, enemydamage, playerdamage, sword
from fightClass import sub_two_player_hp
from level1 import level1
from level2 import level2
from level3 import level3

def main():
    # Level 1
    print("Running Level 1...")
    level1()

    # Level 2
    print("Running Level 2...")
    level2()

    # Level 3
    print("Running Level 3...")
    level3()

if __name__ == '__main__':
    main()
