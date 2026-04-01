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
    
class flower_cards(Card):
    flower_names = ['小王','大王','花牌']
    def __init__(self, flower=0):
        self.flower = flower
    def __str__(self):
        return '%s' % (flower_cards.flower_names[self.flower])
    
class Deck:
    def __init__(self, flower=0):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
        # flower_cards_new = flower_cards()
        if flower != 0:
            for color in range(3):
                flower_card = flower_cards(color)
                self.cards.append(flower_card)

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

    def deal_hands(self, persons, one_hand_card_nums):
        a = []
        for i in range(persons + 1):
            a.append(Hand())
        for i in range(one_hand_card_nums):
            # j = 0
            for i in range(persons):
                self.move_cards(a[i], 1)
                # j += 1
        self.move_cards(a[-1], len(self.cards))
        return a
    
    def cutting_cards(self):
        cutting_nums = random.randint(3, 50)
        bright_card = self.cards[cutting_nums]
        return bright_card

class Hand(Deck):
    def __init__(self, lable=''):
        self.cards = []
        self.lable = lable

# all_cards = Deck(1)
# king_cards = flower_cards()
# all_cards.shuffle()
# t = all_cards.cutting_cards()

# x = all_cards.deal_hands(3, 17)
# j = 0
# for i in x:
#     if j <= 2:
#         print(f'---第{j+1}家牌：---', '\n', end = '')
#         print(i)
#         j +=1
#     else:
#         print(f'---底牌：---', '\n', end = '')
#         print(i)

def dou_di_zhu_fapai():
    all_cards = Deck(1)
    all_cards.shuffle()
    t = all_cards.cutting_cards()
    print('地主牌为%s' % t)
    x = all_cards.deal_hands(3, 17)
    j = 0
    for i in x:
        if j <= 2:
            if t in i.cards:
                print(f'---地主牌为第{j+1}家所有，他具有优先叫牌权：---', '\n', end = '')
                print(i)
            else:
                print(f'---第{j+1}家牌：---', '\n', end = '')
                print(i)
        j += 1
    print(f'---底牌：---', '\n', end = '')
    print(x[-1])

dou_di_zhu_fapai()