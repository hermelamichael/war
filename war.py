import random

class Card():
    def __init__(self,rankvalue,rankname,suit):
        self.rankvalue = rankvalue 
        self.rankname = rankname
        self.suit = suit 
    
    def __it__(self, other):
        return self.rankvalue < other.rankvalue
    
    def __gt__(self, other):
        return self.rankvalue > other.rankvalue

    def __eq__(self, other):
        return self.rankvalue == other.rankvalue

    def __str__(self):
        return self.rankname + " of " + self.suit

def create_deck():
    #creates a deck of cards, which are instances of the card class
    #cards have their own </>/==, which the it/gt/eq methods 
    #xards have their own printanle version, with the str method 
    deck = []

    suits = ("Clubs", "Spades", "Hearts", "Diamonds")
    ranks = ("2", "3", "4", "5", "6", "7", "8","9","10","Jack","Queen","King","Ace")

    for s in suits:
        for i, r in enumerate(ranks):
            deck.append(Card(i+2,r,s))

    return deck

def find_winner(card1, card2):
    if card1 > card2: return "Player one"
    if card1 < card2: return "Player two"
    else: return "No one"

def main():
    deck = create_deck()

    random.shuffle(deck)

    while len(deck) >= 2:

        player_one_card = deck.pop()
        player_two_card = deck.pop()
        winner = find_winner(player_one_card, player_two_card)

        print(f"Player one draws a {player_one_card}")
        print(f"Player two draws a {player_two_card}")
        print(f"{winner} wins")

        input("Press enter to play again\n")
    
    else: print("Deck empty. Goodbye")

main()

