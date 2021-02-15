# Ben Jordan
# 12/9/2020

from random import shuffle
# Only used to associate values
valuesdict = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six': 6,
              'Seven': 7, 'Eight' : 8, 'Nine' : 9, 'Ten': 10, 'Jack': 11, 
              'Queen': 12, 'King' : 13, 'Ace' : 14}

# create card instances
suits = [ "Hearts", "Clubs", "Spades", "Diamonds"]
ranks = list(valuesdict.keys())

# create card class
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank.title()
        self.value = valuesdict[self.rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
         shuffle(self.all_cards)
            
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_card(self):
        
        return self.all_cards.pop(0)
        
    def add_cards(self, new_cards):
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        return f' Player {self.name} has {len(self.all_cards)} cards.'

#Game Logic

# create two players
player1 = Player('One')
player2 = Player('Two')

# Create new deck
new_deck = Deck()
    # shuffle
new_deck.shuffle()
# split deck between each player

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

# check to see if anybody has won/lost (0 cards)
# while game_on is true
round_num = 0
game_on = True
eachwar = 15

while game_on:
    round_num += 1
    print(f'Round {round_num}')
        
    if len(player1.all_cards) == 0:
        print("Player 2 wins!")
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print("Player 1 wins!")
        game_on = False
        break
    player_1_cards = []
    player_1_cards.append(player1.remove_card())
    player_2_cards = []
    player_2_cards.append(player2.remove_card())
    war = True
    while war:
        if player_1_cards[-1].value > player_2_cards[-1].value:
            player1.add_cards(player_1_cards) 
            player1.add_cards(player_2_cards)
            war = False
        elif player_1_cards[-1].value < player_2_cards[-1].value:
            player2.add_cards(player_1_cards) 
            player2.add_cards(player_2_cards)
            
            war = False
        else: 
            print('WAR!')
            if len(player1.all_cards) < eachwar:
                print('Player One unable to declare war.')
                print('Player Two Wins!')
                game_on = False
                war = False
            elif len(player2.all_cards) < eachwar:
                print('Player Two unable to declare war.')
                print('Player One Wins!')
                game_on = False
                war = False
            else:
                for num in range(eachwar):
                    player_1_cards.append(player1.remove_card())
                    player_2_cards.append(player2.remove_card())
