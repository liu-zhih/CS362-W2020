# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:13:42 2020

@author: Zhihui Liu
"""
import testUtility
import Dominion
import random
from collections import defaultdict

#Get player names
player_names = testUtility.GetPlayernames()

#number of curses and victory cards

nV=testUtility.GetnV(player_names)

#-------------------changed data---------------------------
#the following 0 should be the amount of player, while 0 will
#leds to there are no Curse available for the players to buy
nC = testUtility.GetnC(0)
#----------------------------------------------------------

#Define box
box = testUtility.Getbox(nV)

supply_order = testUtility.Getsupply_order()

#The supply always has these cards
supply = testUtility.get_supply(box, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.give_playernames(player_names)

#Play the game
testUtility.play_game(supply, supply_order, players, trash)

#Final score
testUtility.display_winner(players)