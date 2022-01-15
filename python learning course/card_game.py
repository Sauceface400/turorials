import random

#============================VALUE OF THE CARDS===========================
class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value,self.suit))
#==============================MAKING OF THE CARDS===============================
class Deck(object):
    def __init__ (self):
        self.cards = []
        self.build()
    def build(self):
        for s in ("Spades","clubs","Diamonds","Hearts"):
            for v in range(1,14):
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle (self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()
#========================================THE CODE FOR THE PLAYER==============================
class player(object):
    def __init__ (self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard()) 
        return self
    
    def showhand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
#===================FOR THHE CARDS========================
deck = Deck()
deck.shuffle()
deck.show()
#====================================FOR THE PLAYER======================
jabit = player("jabit")
jabit.draw(deck).draw(deck)
jabit.showhand()
#=========================FOR THE CARDS=================================
card = Card("Clubs",6)
card.show()
card = deck.draw()
card.show()
