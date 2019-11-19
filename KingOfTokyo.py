import PySimpleGUI as sg
import playsound
import time
import random



class Player:
    #TODO
    #att: name, monster, cards, energy, roll order?

class Card:
    #TODO
    #att: name, description, abilities, active, inactive, etc
    #how will we apply these abilities to the game?
    #need to implement modifiers somehow
    #will need to run a check for cards in play on each turn and have a system to apply these effects

class Board:
    #TODO
    #lists holding positions of players
    #in tokyo, out of tokyo
    
class Monster:
    #TODO
    #att: name, desc.
    
class Energy:
    #TODO
    #perhaps this class is not needed as it is a simple int, could be an att for player.
    
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
    
def run_game():
    #main game logic
    

    
    
