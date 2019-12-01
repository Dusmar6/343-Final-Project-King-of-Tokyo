
from time import sleep
import random

class Player:

    def __init__(self, monster):
        self.Monster = monster
        self.cards = []
        self.hearts = 10
        self.points = 0
        self.energy = 0
        self.alive = True
        self.in_tokyo = False
        
    #functions
    def get_monster(self):
        return self.Monster
    
    def get_cards(self):
        return self.cards
    
    def get_hearts(self):
        return self.hearts
    
    def get_points(self):
        return self.points
    
    def get_energy(self):
        return self.points
    
    def alive(self):
        return self.alive
    
    def in_tokyo(self):
        return self.in_tokyo
    
    def enter_tokyo(self):
        self.in_tokyo = True
        
    def exit_tokyo(self):
        self.in_tokyo = False
    
    def kill(self):
        self.alive = False
    
    def heal(self, amount):
        if (self.hearts + amount)>10:
            self.hearts = 10
        else:
            self.hearts = self.hearts + amount
       
    def take_damage(self, amount):
        if(amount > self.hearts):
            self.hearts = 0
            self.kill()
        else:
            self.hearts = self.hearts - amount
            
    def add_points(self, amount):
        self.points = self.points + amount
    
    def add_energy(self, amount):
        self.energy = self.energy + amount
        
    def lose_energy(self, amount):
        if(amount > self.energy):
            self.energy = 0
        else:
            self.energy = self.energy - amount
    
    def add_card(self, card):
        if(len(self.cards) > 3):
            return False
        else:
            self.cards.append(card)
            return True
    
    def remove_card(self, card):
        if(len(self.cards) == 0):
            return False
        else:
            self.cards.remove(card)
            return True
    
            

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
    def __init__(self, monster_name, monster_description, monster_sound):
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
    def __init__(self, player_list):
        self.player_list = player_list
        self.current_turn = 0
        self.player_count = len(player_list)
        self.graveyard = []
    
    def __str__(self):
        print("Monsters alive: ")
        print("Current turn: ")
        print("Monsters in Tokyo: ")
        print("Monsters outside Tokyo: ")
        
        
    def kill_player(self, Player):
        self.player_list.remove(Player)
        self.player_count = len(self.player_list)
        self.graveyard.append(Player)
        
    def next_turn(self):
        if self.current_turn == self.player_count-1:
            self.current_turn = 0
        else:
            self.current_turn+=1
            
    def add_points_current_player(self, x):
        self.current_player().add_points(x)
        self.check_win()
        
        
    def add_points_player(self, player, x):
        player.add_points(x)
        self.check_win()
        
        
    def check_win(self):
        for player in self.player_list:
            if player.points>= 20:
                print(player.monster.monster_name, " has reached 20 victory points and has taken over Tokyo!")
                
                
    def check_death(self):
        for p in self.player_list:
            if not p.alive:
                print(p.Monster.monster_name, "has died!")
                self.player_list.remove(p)
                self.graveyard.append(p)
                      
    def players_in_tokyo(self):
        m = []
        for p in self.player_list:
            if p.in_tokyo:
                m.append(p)
        return m
    
    def players_outside_tokyo(self):
        m = []
        for p in self.player_list:
            if p.in_tokyo == False:
                m.append(p)
        return m
    
    def damage_players_in_tokyo(self, x):
        m = self.players_in_tokyo()
        for p in m:
            p.take_damage(x)
        self.check_death()
    
    def damage_players_outside_tokyo(self, x):
        m = self.players_outside_tokyo()
        for p in m:
            p.take_damage(x)
        self.check_death()
        
    def current_player(self):
        return self.player_list[self.current_turn]
    
    def tokyo_full(self):
        if len(self.players_in_tokyo()) < 2:
            return False
        return True
    
    
def load_monsters():
    #Add all the avaliable monsters that are from the game and return an array 
    m = []
    m.append(Monster("Alienoid", "He comes from an ancient alien race, known across the galaxy for their stench!", "Bleh!"))
    m.append(Monster("Cyber Kitty", "A mecha feline with a pink suit of armour and razor sharp claws. Careful she's a bad kitty!", "Meow."))
    m.append(Monster("Giga Zaur", "He's a fearless, cold-blooded, Tokyo-stomping machine. (And some say he's the best kisser). Watch out for this lizard.", "Rawr!"))
    m.append(Monster("Space Penguin", "A penguin? In space? He's the result of a horrific gene-splicing experiment gone wrong involving penguin and space DNA.", "Squeak!"))
    m.append(Monster("Meka Dragon", "Do robot dragons still need to eat? We aren't sure, but you should take a few steps back just to be safe.", "*Dragon Sounds*"))
    m.append(Monster("Mongo", "He has no fear. He has no weaknessess. He's 40 feet tall and is composed of over 90 tons of delicious gingerbread, and he's coming for you.", "Run! Run! As fast as you can!"))
    return m

def pre_div():
    print("\n----------------------------------------")
    
def post_div():
    print("----------------------------------------\n")

def scroll():
    print ("\n"*50)

def setup():
    monsters = load_monsters()
    monsters_playing = []
    scroll()
    pre_div()
    print("Welcome to King Of Tokyo! The aim of the game is to take over Tokyo and earn the most points. \nThe first monster to get 20 victory points is the winner!")
    post_div()
    sleep(1)
    print("Enter the number of players (2-6): ")
    player_count = int(get_input(2,6))
    
    
    for num in range(player_count):
        scroll()
        pre_div()
        for i in range(len(monsters)):
            print(str(i+1)  + ".", monsters[i].monster_name, "\n", " "*3, monsters[i].monster_description, "\n")
            
        post_div()
        print("Player ", num+1, ", select your monster (1-"+ str(len(monsters))+ ").\n")
        choice = get_input(1, len(monsters))
        monsters_playing.append(monsters[choice-1])
        monsters.remove(monsters[choice-1])
        
    
    players = []
    for monster in monsters_playing:
        players.append(Player(monster))
    
    scroll()
    
    for p in players:
        print(p.Monster.monster_name)
        sleep(1)
    print("... Are you ready?", end = " ")
    sleep(1)
    scroll()
    print("""
  _      ______ _______ _____    _____  ____  
 | |    |  ____|__   __/ ____|  / ____|/ __ \ 
 | |    | |__     | | | (___   | |  __| |  | |
 | |    |  __|    | |  \___ \  | | |_ | |  | |
 | |____| |____   | |  ____) | | |__| | |__| |
 |______|______|  |_| |_____/   \_____|\____/ 
                                              
                                              
""")
    sleep(1)
    game_state = GameState(players)
    return game_state
            
def print_dice(rolled):
    
    print("/nYou rolled: ")
    for num in rolled:
        if rolled[num] == 1: print("Victory Point (1)")
        if rolled[num] == 2: print("Victory Point (2)")
        if rolled[num] == 3: print("Victory Point (3)")
        if rolled[num] == 4: print("Attack Damage (1)")
        if rolled[num] == 5: print("Heart (1)")
        if rolled[num] == 6: print("Energy (1)")
    

def roll_dice():
    rolled = []
    for num in range(6):
        rolled[num] = random.randInt(1,6)
    print_dice(rolled)
    rolled = re_roll(rolled)
    print_dice(rolled)
    rolled = re_roll(rolled)
    return resolve_dice(rolled)
    

    
def re_roll(rolled):
    print("/nEnter the dice you wish to reroll (1234): ")
    re = str(input())
    for num in range(1,7):
        if str(num) in re: rolled[num-1] = random.randInt(1,6)
    return rolled  
    
    
def resolve_dice(rolled):
    points = 0
    damage = 0
    heal = 0
    energy = 0
    
    for num in range(1, 4):
        if rolled.count(num)>=3:
            points+= num
            if rolled.count(num)>3:

                points+= rolled.count(num)-3
                
    damage+= rolled.count(4)
    heal+= rolled.count(5)
    energy+= rolled.count(6)
    
    
    
    return points, heal, damage, energy

    




#def buy_card():
    #subtracts energy
    #gives player a card
    
def get_input(min_inp, max_inp):
    if(min_inp == 0 and max_inp == 0): 

        user_Input = input("")
        while(len(user_Input) < 1):
            print("Please enter a valid input" )
            user_Input = input("")
    else:

        user_Input = int(input())
        while(user_Input < min_inp or user_Input > max_inp):
            print("Please enter a valid input" )
            user_Input = int(input())
    return user_Input

def randomize(x):
    return random.shuffle(x)

#    
#def deal_damage():
#    #takes location of the monsters as parameter (inside,outside)
#    #checks if monster is alive upon damage. if dead. run kill monster
#    
#def kill_monster():
    #takes monster as parameter. removes him from the game
    
    
    
    
def run_game(state):
    
    winner = None
    while winner == None:
        scroll()
        
        
        print(state.current_player().Monster.monster_sound, "It's", state.current_player().Monster.monster_name+"'s turn!" )
        if state.current_player().in_tokyo():
            print("You gained 2 Victory Points for starting your turn already in Tokyo!")
            state.add_points_current_player(2)
        if not state.tokyo_full():
            state.current_player().enter_tokyo()
            print("\n--", state.current_player().Monster.monster_name, "has invaded Tokyo! --")
            
        print("\nMonsters in Tokyo: ")
        m = state.players_in_tokyo()
        for p in m:
            print( p.Monster.monster_name, "- VICTORY POINTS:", p.get_points(), "HEARTS:", p.get_hearts())
        
        print("\nMonsters outside Tokyo: ")
        m = state.players_outside_tokyo()
        for p in m:
            print( p.Monster.monster_name, "- VICTORY POINTS:", p.get_points(), "HEARTS:", p.get_hearts())
            
        
        print("\n--Press enter to roll dice--")
        k = input()
        results = roll_dice()
        
        points = results[0]
        heal   = results[1]
        damage = results[2]
        energy = results[3]
        
        print("\n", state.current_player().Monster.monster_name, "earned", points, "victory points.")
        state.add_points_current_player(points)
        
        if not state.current_player().in_tokyo():
            print("\n", state.current_player().Monster.monster_name, "healed", heal, "hearts.")
            state.current_player().heal(heal)
            
        print("\n", state.current_player().Monster.monster_name, "gained", energy, "energy.")
        state.current_player().add_energy(energy)
        
        
        if state.current_player().in_tokyo():
            print("\n", state.current_player().Monster.monster_name, "dealt", damage, "to monsters outside Tokyo.")
            state.damage_players_outside_tokyo(damage)
                
        else:
            print("\n", state.current_player().Monster.monster_name, "dealt", damage, "to monsters inside Tokyo.")
            state.damage_players__tokyo(damage)
        
        
        
        
        state.next_turn()
        
    
def main():
    run_game(setup())
    
    
    
    
main()






















