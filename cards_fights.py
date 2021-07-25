from random import shuffle
import os

cards_basic = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jopek', 'Dama', 'Król', 'As', 'Joker']
deck_pOne = []+cards_basic*4
deck_pTwo = []+cards_basic*4
shuffle(deck_pOne)
shuffle(deck_pTwo)
field_pOne = []
field_pTwo = []

# Temporary function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_terminal()
