import random

class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['梅花', '方块', '红桃', '黑桃']
    rank_names = [None, '2', '3', '4', '5',
                  '6', '7', '8', '9', '10',
                  'J', 'Q', 'K', 'A']
    def __str__(self):
        return '%s%s' % (Card.suit_names[self.suit], Card.rank_names[self.rank])
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        i = 1
        for card in self.cards:
            res.append(str(i) + ':' + str(card))
            i += 1
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_deck(self):
        self.cards.sort(reverse=False)
        return self
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
            
class Hand(Deck):
    def __init__(self, lable=''):
        self.cards = []
        self.lable = lable

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __lt__(self, other):
        try:
            t1 = self.hour, self.minute, self.second
            t2 = other.hour, other.minute, other.second
            return t1 < t2
        except:
            return '大哥你输入的Time类吗？'


deck = Deck()
deck.shuffle()
print(deck.cards[0])
# print('---')
# print(deck.sort_deck())