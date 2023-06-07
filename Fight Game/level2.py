import time
import random
from playerAtributes import player1, player3, enemydamage, playerdamage, sword
from fightClass import sub_two_player_hp

def repeat():
    while True:
        player1.hitpoints = player1.maxhp
        player3.hitpoints = player3.maxhp
        print("Starting a new fight...")
        time.sleep(2)

        while True:
            player3.hitpoints = sub_two_player_hp(player3, playerdamage)
            print("You gave: " + str(playerdamage) + " damage "  + str(sword) + " and sword damage")
            print("Enemy's health is now: " + str(player3.hitpoints))
            time.sleep(1)

            player1.hitpoints = sub_two_player_hp(player1, enemydamage)
            print("You got: " + str(enemydamage) + " damage " + str(sword) + " and sword damage")
            print("Your health is now: " + str(player1.hitpoints))
            time.sleep(1)

            if player1.hitpoints <= 0:
                print("You lost. Your health is 0.")
                break
            if player3.hitpoints <= 0:
                print("You won! Enemy's hp is 0.")
                return

while True:
    player3.hitpoints = sub_two_player_hp(player3, playerdamage)
    print("You gave: " + str(playerdamage) +  " damage "  + str(sword) + " and sword damage")
    print("Enemy's health is now: " + str(player3.hitpoints))
    time.sleep(1)

    player1.hitpoints = sub_two_player_hp(player1, enemydamage)
    print("You got: " + str(enemydamage) + " damage "  + str(sword) + " and sword damage")
    print("Your health is now: " + str(player1.hitpoints))
    time.sleep(1)
    if player1.hitpoints <= 0 == 0:
        print("You lost. Your health is 0.")
        repeat()
    if player3.hitpoints <= 0 == 0:
        print("You won! Enemy's hp is 0.")
        break
