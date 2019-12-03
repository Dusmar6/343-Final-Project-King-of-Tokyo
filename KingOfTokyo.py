
from time import sleep
import random



cards = []






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
    
    def remove_card_by_name(self, name):
        if(len(self.cards) == 0):
            return False
        else:
            c = self.get_cards()
            for card in c:
                if card.name == name:
                    self.cards.remove(card)
        
        
    def has(self, name):
        c = self.get_cards() 
        for card in c:
            if card.name == name:
                return True
        return False
    
    def remove_all_cards(self):
        self.cards = []            

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
        self.deck = []
    
        
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
                print("""

   _____ ____  _   _  _____ _____         _______ _____ 
  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____|
 | |   | |  | |  \| | |  __| |__) |   /  \  | | | (___  
 | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \ 
 | |___| |__| | |\  | |__| | | \ \  / ____ \| |  ____) |
  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_| |_____/ 
                                                        
                                    """                    
)
                print("\n\nPlay again? (y/n)")
                inp = input()
                if inp == "y" or inp == "yes":
                    main()
                else:
                    sys.exit(0)
                
    def check_death(self):
        for p in self.player_list:
            if not p.alive:
                print("\n--",p.Monster.monster_name, "has died! You are out of the game.--")
                if p.has("Martyr"):
                    print("\n--Martyr has been activated!")
                    if p.in_tokyo():
                        for player in self.players_in_tokyo():
                            player.heal(3)
                    if not p.in_tokyo():
                        for player in self.players_outside_tokyo():
                            player.heal(3)
                self.player_list.remove(p)
                self.graveyard.append(p)
             
                
    def players_in_tokyo(self):
        m = []
        for p in self.player_list:
            if p.alive:
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
        if x>0:
            m = self.players_in_tokyo()
            if self.current_player().has("Sharpened Claws"):
                x+=2
            for p in m:
                if p.has("Armored Scales"):
                    x=x-1
                p.take_damage(x)
            self.check_death()
    
    def damage_players_outside_tokyo(self, x):
        if x>0:
            m = self.players_outside_tokyo()
            if self.current_player().has("Sharpened Claws"):
                x+=2
            for p in m:
                if p.has("Armored Scales"):
                    x=x-1
                p.take_damage(x)
            self.check_death()
        
    def current_player(self):
        return self.player_list[self.current_turn]
    
    def tokyo_full(self):
        if self.player_count>3:
            if len(self.players_in_tokyo()) < 2:
                return False
            return True
        if self.player_count<=3:
            if len(self.players_in_tokyo()) < 1:
                return False
            return True
    
    def fill_deck(self):
        cards = randomize(load_cards())
        while len(self.deck)<3:
            c = cards[random.randint(0, len(cards)-1)]
            if c not in self.deck:
                self.deck.append(c)


    
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

def load_cards():
    c = []
    c.append(Card("High Roller", 8, "d", "Discard: Purchase this card to do the dice section twice this turn.")) #
    c.append(Card("Sharpened Claws", 8, "k", "Keep: Purchase this card to do 2 extra damage each turn till the end of the game."))#
    c.append(Card("Stink Bomb", 4, "d", "Discard: Purchase this card to immediately kick all monsters out of Tokyo.")) #run
    c.append(Card("Martyr", 3, "k", "Keep: If you die, all monsters in your area heal 3 hearts."))#
    c.append(Card("First Bathing Ritual", 5, "d", "Discard: Purchase this card to cleanse all other monsters of their keep cards, as well as refresh the 3 available cards for purchase.")) #run
    c.append(Card("Second Bathing Ritual", 3, "d", "Discard: Purchase this card to cleanse yourself of your keep cards, as well as refresh the 3 available cards for purchase.")) #run
    c.append(Card("Tables Turned", 5, "d", "Discard: Purchase this card to immediately deal 2 damage to monsters in your area.")) #run
    c.append(Card("Rolling Thunder", 8, "d", "Discard: Purchase this card to do 3x damage this turn."))#
    c.append(Card("Sustained Fire", 7, "k", "Keep: Purchase this card to do 1 extra damage each turn till the end of the game."))#
    c.append(Card("Revert", 6, "d", "Discard: Purchase this card to reverse the turn order."))#run
    c.append(Card("Powerbunny", 7, "k", "Keep: Purchase this card to gain an extra energy each round."))#
    c.append(Card("Filibuster" , 7, "d", "Discard: Purchase this card to skip the next player's turn."))#
    c.append(Card("Hate Healer", 8, "d", "Discard: Purchase this card to deal damage for every heart you roll this round."))#
    c.append(Card("Power Play", 9, "d", "Discard: Sacrifice a victory point to deal 2 damage to ALL other monsters."))#run
    c.append(Card("Precision Strike", 11, "d", "Discard: Deal 5 damage to a monster of your choice."))#run
    c.append(Card("Prime Engram", 7, "d", "Discard: This card immediately grants you 3 victory points."))#run
    c.append(Card("Armored Scales", 6, "k", "Keep: All damage is reduced by 1."))#
    return c
    
    
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
    
    print("\nYou rolled: ")
    for num in range(len(rolled)):
        print(str(num+1)+". ", end='')
        if rolled[num] == 1: print("Victory Point (1)")
        if rolled[num] == 2: print("Victory Point (2)")
        if rolled[num] == 3: print("Victory Point (3)")
        if rolled[num] == 4: print("Attack Damage (1)")
        if rolled[num] == 5: print("Heart (1)")
        if rolled[num] == 6: print("Energy (1)")
    

def roll_dice():
    rolled = []
    for num in range(6):
        rolled.append(random.randint(1,6))
    print_dice(rolled)
    
    rolled = re_roll(rolled)
    print_dice(rolled)
    print("\nLast Reroll!")
    rolled = re_roll(rolled)
    return resolve_dice(rolled)
    

    
def re_roll(rolled):
    print("\nEnter the dice you wish to reroll (i.e type 124 to re-roll dice 1, 2, and 4): ")
    re = str(input())
    for num in range(1,7):
        if str(num) in re: rolled[num-1] = random.randint(1,6)
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
    
    print_dice(rolled)
    
    return points, heal, damage, energy


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
    random.shuffle(x)
    return x

def buy(state, pick):
    global cards
    if state.deck[pick-1].card_type == "d" or len(state.current_player().cards)<3:
        if state.deck[pick-1] not in state.current_player().cards:
            if state.current_player().energy >= state.deck[pick-1].cost:
                state.current_player().lose_energy(state.deck[pick-1].cost)
                
                if state.deck[pick-1].name in ["High Roller","Sharpened Claws","Martyr", "Rolling Thunder", "Sustained Fire", "Powerbunny", "Filibuster", "Hate Healer","Armored Scales" ]:
                    state.current_player().add_card(state.deck[pick-1])
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
                
                elif state.deck[pick-1].name == "Stink Bomb":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    p = state.players_in_tokyo()
                    for player in p:
                        player.exit_tokyo()
                        print(player.Monster.monster_name, "has been kicked out of Tokyo!")
                        
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
                        
                elif state.deck[pick-1].name == "First Bathing Ritual":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("--Monsters have been cleansed--")
                    for p in state.player_list:
                        if p != state.current_player():
                            p.remove_all_cards()
         
                    state.deck.clear()
                    state.fill_deck()
                    return True
                    
                elif state.deck[pick-1].name == "Second Bathing Ritual":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("--You have been cleansed--")
                    state.current_player().cards = []
                    state.deck.clear()
                    state.fill_deck()
                    return True
                
                elif state.deck[pick-1].name == "Tables Turned":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("-- You've turned the tables on your fellow monsters! --")
                    if state.current_player().in_tokyo():
                        for p in state.players_in_tokyo():
                            if p!= state.current_player():
                                p.take_damage(2)
                                
                    if not state.current_player().in_tokyo():
                        for p in state.players_outside_tokyo():
                            if p!= state.current_player():
                                p.take_damage(2)
                    state.check_death()
                            
                    
                    
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
                
                
                elif state.deck[pick-1].name == "Revert":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("-- The play order has been reversed --")
                    state.player_list.reverse()
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
            
                elif state.deck[pick-1].name == "Power Play":
                    if state.current_player().points<2:
                        return False
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("-- You've sacrificed a victory point to damage all other monsters --")
                    state.current_player().points = state.current_player().points-2
                    for p in state.player_list():
                        if p != state.current_player():
                            p.take_damage(2)
                    state.check_death()
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
                
                elif state.deck[pick-1].name == "Precision Strike":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("\n-- Choose the player you wish to strike! --")
                    for num in range(len(state.player_list(0))):
                        print(str(num+1)+".", state.player_list(num))
                        
                    don = get_input(1, state.player_count)
                    
                    state.player_list(don-1).take_damage(5)
                    
                    state.check_death()
                    
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
                
                elif state.deck[pick-1].name == "Prime Engram":
                    print("\n-- You've bought", state.deck[pick-1].name+". --")
                    print("\n-- You have been granted 3 victory points! --")
                    state.add_points_current_player(3)
                    state.deck.pop(pick-1)
                    state.fill_deck()
                    return True
        
    
    
def run_game(state):
    global cards

    state.fill_deck()
    
    winner = None
    while winner == None:
        scroll()
        
        print("""
              
  _  _______ _   _  _____     ____  ______   _______ ____  _  ____     ______  
 | |/ /_   _| \ | |/ ____|   / __ \|  ____| |__   __/ __ \| |/ /\ \   / / __ \ 
 | ' /  | | |  \| | |  __   | |  | | |__       | | | |  | | ' /  \ \_/ / |  | |
 |  <   | | | . ` | | |_ |  | |  | |  __|      | | | |  | |  <    \   /| |  | |
 | . \ _| |_| |\  | |__| |  | |__| | |         | | | |__| | . \    | | | |__| |
 |_|\_\_____|_| \_|\_____|   \____/|_|         |_|  \____/|_|\_\   |_|  \____/ 
                                                                               
                                                                               
""")
        print("\n\n",state.current_player().Monster.monster_sound, "It's", state.current_player().Monster.monster_name+"'s turn!" )
        sleep(1)
        if state.current_player().in_tokyo:
            print("You gained 2 Victory Points for starting your turn already in Tokyo!")
            state.add_points_current_player(2)
        if not state.tokyo_full():
            state.current_player().enter_tokyo()
            print("\n--", state.current_player().Monster.monster_name, "has invaded Tokyo! --")
            
        pre_div()
        print("Cards Available:")
        for card in state.deck:
            print(card.name, "-", card.ability_desc)
        post_div()
        
        print("\n--- Monsters in Tokyo: ")
        m = state.players_in_tokyo()
        for p in m:
            print( p.Monster.monster_name, "- VICTORY POINTS:", p.get_points(), "/20  HEARTS:", p.get_hearts(), "ENERGY:", p.get_energy())
            print( p.Monster.monster_name+"'s cards:" )
            for card in p.cards:
                print(card.name, "-", card.ability_desc)
            print("\n")
        
        print("\n--- Monsters outside Tokyo: ")
        m = state.players_outside_tokyo()
        for p in m:
            print( p.Monster.monster_name, "- VICTORY POINTS:", p.get_points(), "/20  HEARTS:", p.get_hearts(), "ENERGY:", p.get_energy())
            print( p.Monster.monster_name+"'s cards:" )
            for card in p.cards:
                print(card.name, "-", card.ability_desc)
            print("\n")
        
        sleep(1)
        
      
        print("\n\n1. Buy a card\n2. Skip the card menu and roll dice")
        
        pick = get_input(1,2)
        if pick == 1:
            cont = True
            scroll()
            while cont:
                
                print("Which card would you like to buy? Keep in mind, Keep cards stay with you until the end (or until they are removed by a Bathing Ritual card).\n")
                
                for num in range(len(state.deck)):
                    print(str(num+1)+".", "(",state.deck[num].cost,")", state.deck[num].name, "-", state.deck[num].ability_desc)
                print("4. Exit and roll dice.")
                choose = get_input(1,4)
                
                if choose == 1:
                    if buy(state, 1):
                        cont = False
                        break
                    else:
                         print("\n\nUnable to purchase card. Make sure you have enough energy and that you have room if its a keep card.\n\n\n")
                if choose == 2:
                    if buy(state, 1):
                        cont = False
                        break
                    else:
                         print("\n\nUnable to purchase card. Make sure you have enough energy and that you have room if its a keep card.\n\n\n")
                if choose == 3:
                    if buy(state, 1):
                        cont = False
                        break
                    else:
                         print("\n\nUnable to purchase card. Make sure you have enough energy and that you have room if its a keep card.\n\n\n")
                if choose == 4:
                    cont = False
                    break;
        
        n = 1
        
        if state.current_player().has("High Roller"):
            n = 2
            state.current_player().remove_card_by_name("High Roller")
       
        
        
        for num in range(0,n):
            print("\n--Time to roll! Press enter to roll dice--")
            k = input()
    
            results = roll_dice()
            
            points = results[0]
            heal   = results[1]
            damage = results[2]
            energy = results[3]
    
            if state.current_player().has("Rolling Thunder"):
                damage = damage*3
                state.current_player().remove_card_by_name("Rolling Thunder")
            
            if state.current_player().has("Sustained Fire"):
                damage = damage+1
            
            if state.current_player().has("Power Bunny"):
                energy = energy+1

            if state.current_player().has("Hate Healer"):
                damage+= heal
                state.current_player().remove_card_by_name("Hate Healer")
            
            pre_div()
            print("\n---", state.current_player().Monster.monster_name, "earned", points, "victory points.---")
            state.add_points_current_player(points)
            
            if not state.current_player().in_tokyo:
                print("\n---", state.current_player().Monster.monster_name, "healed", heal, "hearts.---")
                state.current_player().heal(heal)
                
            print("\n---", state.current_player().Monster.monster_name, "gained", energy, "energy.---")
            state.current_player().add_energy(energy)
            
            
            if state.current_player().in_tokyo:
                print("\n---", state.current_player().Monster.monster_name, "dealt", damage, "damage to monsters outside Tokyo.---")
                state.damage_players_outside_tokyo(damage)
                    
            else:
                print("\n---", state.current_player().Monster.monster_name, "dealt", damage, "damage to monsters inside Tokyo.---")
                state.damage_players_in_tokyo(damage)
                for p in state.players_in_tokyo():
                    print("\n", p.Monster.monster_name, "has taken damage. Would",p.Monster.monster_name,"like to leave Tokyo? (type 'yes' for yes, simply hit enter if no)")
                    answer = input()
                    if answer == "yes":
                        p.exit_tokyo()
                        print("\n--", p.Monster.monster_name, "has left Tokyo...--")
            post_div()
        print("\nPress enter to continue")
        k = input()
        
        sleep(5)
        if state.current_player().has("Filibuster"):
            state.next_turn()
        state.next_turn()
        

    
def main():
    run_game(setup())
    
    
    
    
main()


