#Core of fighthing system
from playerAtributes import player1, player2, enemydamage, playerdamage, sword
import random
import time


def sub_two_player_hp(player, damage,):
    player.hitpoints -= damage + sword
    
    return player.hitpoints



    


