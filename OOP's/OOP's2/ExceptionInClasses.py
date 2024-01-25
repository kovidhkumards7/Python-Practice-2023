class CreditCard():
    def __init__(self,card_no,bal):
        self.card_no = card_no
        self.bal = bal

class Customer():
    def __init__(self,cards):
        self.cards = cards

    def pur(self,pri,card_no):
        if pri < 0:
            raise Exception
        elif card_no not in self.cards:
            raise Exception
        elif pri > self.cards[card_no].bal:
            raise Exception
        else:
            print("Purchase succesful")

card1 = CreditCard(101,800)
card2 = CreditCard(102,2000)

cards = {card1.card_no:card1,card2.card_no:card2}
c = Customer(cards)

while True:
    card_no = int(input("Enter card no: "))
    try:
        c.pur(1200,card_no)
        break
    except Exception as e:
        print("card not valid or something went wrong " + str(e))
