# AUTOGENERATED! DO NOT EDIT! File to edit: ../card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../card.ipynb 2
from fastcore.all import patch

# %% ../card.ipynb 3
suits = ["♣️","♦️","❤️","♠️"]
ranks = [None, "A"] + [str(x) for x in range(2,11)]  + ["J", "Q", "K"]

# %% ../card.ipynb 4
class Card:
    "A playing card"
    def __init__(self,
                 suit:int,  # An index into `suits`
                 rank:int): # An index into `ranks`
        self.suit,self.rank = suit,rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    def __lt__(self, a): return (self.suit,self.rank)<(a.suit,a.rank)
    def __gt__(self, a): return (self.suit,self.rank)>(a.suit,a.rank)
    __repr__ = __str__
    def j(): print('hello')

# %% ../card.ipynb 9
@patch
def __eq__(self:Card, a): return (self.suit,self.rank)==(a.suit,a.rank)
