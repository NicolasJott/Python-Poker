import random
class pokerCards:

    def __init__(self):

        self.cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.all_cards = []

        #self.all_cards = pass # new function



    # create a new function to create a 5 card hand wih no
    # duplicates, and will 11, 12 etc to jack, queen etc...
    #You need to keep the self.cards value

    def Hand(self):
        while True:
            for i in range(5):
                x = random.randint(0,12)
                y = random.randint(0,3)
                if x > 8:
                    if x == 9:
                        rank = "Jack"
                        self.all_cards.append(rank +' of '+self.suit[y])
                    elif x == 10:
                        rank = "Queen"
                        self.all_cards.append(rank +' of '+ self.suit[y])
                    elif x == 11:
                        rank = "King"
                        self.all_cards.append(rank +' of '+ self.suit[y])
                    elif x == 12:
                        rank = "Ace"
                        self.all_cards.append(rank +' of '+ self.suit[y])
                else:
                    self.all_cards.append(str(self.cards[x]) +' of '+ self.suit[y])
            if self.all_cards[0] == self.all_cards[1] or self.all_cards[0] == self.all_cards[2] or self.all_cards[0] == self.all_cards[3] or self.all_cards[0] == self.all_cards[4]:
                self.all_cards.clear()
            elif self.all_cards[1] == self.all_cards[0] or self.all_cards[1] == self.all_cards[2] or self.all_cards[1] == self.all_cards[3] or self.all_cards[1] == self.all_cards[4]:
                self.all_cards.clear()
            elif self.all_cards[2] == self.all_cards[0] or self.all_cards[2] == self.all_cards[1] or self.all_cards[2] == self.all_cards[3] or self.all_cards[2] == self.all_cards[4]:
                self.all_cards.clear()
            elif self.all_cards[3] == self.all_cards[0] or self.all_cards[3] == self.all_cards[1] or self.all_cards[3] == self.all_cards[2] or self.all_cards[3] == self.all_cards[4]:
                self.all_cards.clear()
            elif self.all_cards[4] == self.all_cards[0] or self.all_cards[4] == self.all_cards[1] or self.all_cards[4] == self.all_cards[2] or self.all_cards[4] == self.all_cards[3]:
                self.all_cards.clear()
            else:
                break


instance = pokerCards()
instance.Hand()
print(*instance.all_cards, sep = ", ")
