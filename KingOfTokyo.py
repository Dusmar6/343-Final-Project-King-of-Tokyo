import PySimpleGUI as sg
import playsound
import time
import random



class Player:
    #TODO
    #att: Monster (single monster object), Cards (list of Card Objects, init to empty), hearts (int, init to 10), points (int, init to 0), energy (int, init to 0), alive (bool, init to 0), in_tokyo (bool, init to false)
    #object is created by passing only a monster object to constructor.
    #basic setters and getters for all
    #make functions: add_card(card object), remove_card(card object). if succesful, return 1, if unsuccesful (like removing a card from an empty list), return -1
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
    
    #will need to run a check for cards in play on each turn and have a system to apply these effects, needs extra attributes to implement effects

    
class Monster:
    def init(self, monster_name, monster_description, monster_sound):
        self.monster_name = monster_name
        self.monster_description = monster_description
        self.monster_sound = monster_sound

    def get_monster_name(self):
        return self.monster_name

    def get_monster_description(self):
        return self.monster_description

    def get_monster_sound(self):
        return self.monster_sound
    
class GameState:
    #TODO
    #Holds all the players, current turn, board positions, etc..
    #player count (int)
    #graveyard (list monster) dead players, removed from players
    #players (list player in order of roll order)
    #active_cards (list Card) #think of ways to implement. Needs to run check each round for modifiers... 
    
def load_monsters():
    m = []
    m.add(new Monster("Alienoid", "He comes from an ancient alien race, known across the galaxy for their stench!", "Bleh!"))
    m.add(new Monster("...."))
    #add rest... get info from user guide
    
    
    return m

def setup():
    #get # of players, monsters, roll order
    #load into objects, return gamestate to run game
    #put into a pysimpleGUI if enough time
    
def roll_dice():
    #will be a fairly complex system to run the dice roll functionality
    #implement after game logic so it meshes well

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

def checkWin():
    #checks gamestate to see if a player has won
    #called by run_game
    
def deal_damage():
    #takes location of the monsters as parameter (inside,outside)
    #checks if monster is alive upon damage. if dead. run kill monster
    
def kill_monster():
    #takes monster as parameter. removes him from the game
    
def run_game():
    #main game logic
    

    
    
