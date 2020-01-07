import cards
import random

class PLAYER:
    """here is where the players are created, assigned thier cards, etc"""

    def __init__(self, name,):
        self.name = name        #assigns the name of the player
        self.cards = []
        self.is_card_czar = False 
        self.chosen_card = ''
        self.points = 0       

    def assign_cards(self, card):
        self.cards.append(card)

    def toggle_card_czar(self):
        self.is_card_czar = not self.is_card_czar    #makes the player the card czar     
    
    def choose(self, choice):
        self.chosen_card += (self.cards.pop(choice))

    def give_point(self):
        self.points += 1

    def clear_choice(self):
        cards.WHITE.append(self.chosen_card)    #before clearing, it puts the card into WHITE list so that it can be reused
        self.chosen_card = ''
    
    def get_card(self):
        self.cards.append(cards.WHITE.pop(random.randint(0,len(cards.WHITE)-1)))  #gets a random card from the WHITE list


