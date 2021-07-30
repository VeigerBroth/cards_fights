from random import shuffle, randint
import os

def enter_value(input_message, error_message, input_type_convertion, 
                first_condition_value=None, second_condition_value=None):
                    
    while True:
        try:
            if input_type_convertion == int:
                enter_value = int(input(input_message))
                if enter_value <= first_condition_value \
                and enter_value != second_condition_value:
                    break
                else:
                    print(error_message)
        except:
            print(error_message)
            
    return enter_value
    
def start_minigame():
    start_game = None
    print('To know, who start - you or your enemy - you will play to guess a number from 1 to 10.')
    
    for i in range(start_value):
        guess_value = enter_value(f'Player {i+1} guess a number: ',
        'Incorrect value - choose only numbers from 1 to 10.', int, 10, 0)
        
        # True only for PvP and first iteration of for loop
        if i==0 and start_value==2:
            guess_value_first = guess_value
        elif i==1 and guess_value_first==guess_value:
            print('Enter value cant be the same - choose again!')
            start_minigame()
            
    if start_value==2:
        result_first = abs(guess_value_first - number_to_guess)
        
    result_second = abs(guess_value - number_to_guess)
    
    if start_value==2:
        if result_first < result_second:
            # Win first player
            print('First player start the game!')
            start_game = 1
        elif result_first > result_second:
            print('Second player start the game!')
            # Win second player
            start_game = 0
            
    elif start_value==1:
        pc_guess_number = pc_start_guess_number(result_second)

        if result_second < pc_guess_number:
            print('Player start the game!')
            start_game = 1
        elif result_second > pc_guess_number:
            print('PC start the game!')
            start_game = 0

    return start_game

def pc_start_guess_number(player_number):
    pc_guess_number = randint(1, 10)

    if player_number!=pc_guess_number:
        return pc_guess_number
    else:
        return pc_start_guess_number(player_number)

# Temporary function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cards_basic = ['2', '3', '4', '5', '6', '7', '8', '9', 
               '10', 'Jack', 'Queen', 'King', 'Ace', 'Joker']
               
deck_pOne = []+cards_basic*4
deck_pTwo = []+cards_basic*4
shuffle(deck_pOne)
shuffle(deck_pTwo)
field_pOne = []
field_pTwo = []
number_to_guess = randint(1, 10)
clear_terminal()


start_value = enter_value('Choose number from 1 to 3.\n1 - play with PC; 2 - play with other player; 3 - quit game. ',
'Incorrect value - choose only numbers from 1 to 3.', int, 3, 0)

if start_value==1 or start_value==2:
    start_player = start_minigame()

elif start_value==3:
    print('Game exit...')
    quit()
