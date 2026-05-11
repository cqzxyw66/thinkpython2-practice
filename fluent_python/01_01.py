#! /bin/env/python3
#! -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '黑桃 梅花 方块 红桃'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
suit_values = dict(黑桃=3, 红桃=2, 方块=1, 梅花=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    
if __name__ == "__main__":
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high, reverse=True):
        print(card)