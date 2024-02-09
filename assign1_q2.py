import random
class Card:

    def __init__(self, rank = "", suit = ""):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    

class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Clubs', 'Diamonds', 'Hearts','Spades' ]

    def __init__(self,cards=[]):
        self.cards= cards
        self.card_obj()
        self.shuffle()

    def card_obj(self):
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
       random.shuffle(self.cards)

    def total_cards(self):
        return len(self.cards)
    
    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

def main():
    deck=Deck()
    print("Card Dealer")
    print()
    print("I have shuffled a deck of ", deck.total_cards(), " cards.")
    print()
    card_num = int(input("How many cards would you like?: "))
    print()
    print("Here are your cards:")
    for i in range(card_num):
        card = deck.deal_card()
        if card: 
            print(card)
        else:
            print("No more cards to deal.")
            break  
    print()
    print("There are ", str(deck.total_cards()), " cards left in the deck.")
    print()
    print("Good Luck!")

main()


  



