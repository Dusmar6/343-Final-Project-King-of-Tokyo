import PySimpleGUI as sg
import playsound
import time
import random



class Player:
    #TODO
    #att: Monster (single monster object), Cards (list of Card Objects, init to empty), hearts (int, init to 10), points (int, init to 0), energy (int, init to 0), alive (bool, init to true)
    #object is created by passing only a monster object to constructor.
    #basic setters and getters for all
    #for Cards, make functions: add_card(card object), remove_card(card object). if succesful, return 1, if unsuccesful (like removing a card from an empty list), return -1
    #for Hearts, Points, Energy: make functions that increase and decrease the amount by a given parameter (i.e add_heart(int)).
    #   make sure Points and Energy cannot go below 0. If hearts goes below 0, set alive attribute to false

class Card:
    def __init__(self, name, cost, card_type, ability_desc):
        self.name = name
        self.cost = int(cost)
        self.card_type = card_type
        self.ability_desc = ability_desc

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_card_type(self):
        return self.card_type

    def get_ability_desc(self):
        return self.ability_desc
    
    #will need to run a check for cards in play on each turn and have a system to apply these effects

    
class Monster:
    #TODO
    #att: name (string), desc(string), character_sound (string) )
    #no setters, just getters.
    
class GameState:
    #TODO
    #Holds all the players, current turn, board positions, etc..

def setup():
    #get # of players, names, monsters, roll order
    #load into objects, return gamestate to run game
    #put into a pysimpleGUI if enough time
    
def roll_dice():
    #will be a fairly complex system to run the dice roll functionality

def buy_card():
    #subtracts energy
    #gives player a card
    
def get_input(min_inp, max_inp):
    if(min_inp == 0 and max_inp == 0): 
        user_Input = input("")
        while(len(user_Input) < 1):
            print("Please enter a valid input" )
            user_Input = input("")
    else:
        while(user_Input < min_inp and user_Input > max_inp):
            print("Please enter a valid input" )
            user_Input = input("")
    return user_Input

def randomize(x):
    return random.shuffle(x)

def run_game():
    #main game logic
    

    
    
