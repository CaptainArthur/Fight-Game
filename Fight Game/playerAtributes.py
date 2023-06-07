#This program gives Player atributes
from HumanPlayerClass import Player
import random

#Names doesn't do anything and it's prepared for the next versions of game
player1 = Player("Adam", 10, 10)
player2 = Player("EnemyLVL1",10, 10)
player3 = Player("EnemyLVL2",12, 12)
player4 = Player("EnemyLVL3",15, 15)

enemydamage = random.randint(1,5)
playerdamage = random.randint(1,5)
sword = 1 #This is preparation for the shop/lvlup system

