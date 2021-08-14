from random import shuffle, randint
import os

def enter_value(input_message, error_message, input_type_convertion, 
                first_condition_value=None, second_condition_value=None):
                    
    while True:
        try:
            if input_type_convertion == int:
                enter_value = int(input(input_message))
                if enter_value <= first_condition_value \
                and enter_value > second_condition_value:
                    break
                else:
                    print(error_message)
        except:
            print(error_message)
            
    return enter_value
    
def start_minigame(start_value):
    start_game=None
    print('To know, who start - you or your enemy -' 
    +' you will play to guess a number from 1 to 10.')
    
    for i in range(start_value):
        guess_value = enter_value(f'Player {i+1} guess a number: ',
        'Incorrect value - choose only numbers from 1 to 10.', int, 10, 0)
        
        # True only for PvP and first iteration of for loop
        if i==0 and start_value==2:
            guess_value_first = guess_value
        elif i==1 and guess_value_first==guess_value:
            print('Enter value cant be the same - choose again!')
            return start_minigame(start_value)
            
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
      
def add_cards_from_deck_to_hand(hand, deck, t):
    for i in range(t):
        hand.append(deck[0])
        deck.remove(deck[0])
        
def add_cards_from_hand_to_field(field_name, field_str, hand, t):
        field_str.append(hand[t-1])
        field_name.append(hand[t-1])
        hand.remove(hand[t-1])
        
def show_card_in_field(field_card_name, field_card_str):
    print(('-'*13+' ')*(len(field_card_name)))

    for i in range(len(field_card_name)):
        if field_card_name[i]==11:
            print('-'+'Jack'.center(11)+'- ', end='')
        elif field_card_name[i]==12:
            print('-'+'Queen'.center(11)+'- ', end='')
        elif field_card_name[i]==13:
            print('-'+'King'.center(11)+'- ', end='')
        elif field_card_name[i]==14:
            print('-'+'Ace'.center(11)+'- ', end='')
        elif field_card_name[i]==15:
            print('-'+'Joker'.center(11)+'- ', end='')
        else:    
            print('-'+str(field_card_name[i]).center(11)+'- ', end='')

    print('\n'+('-'+' '*11+'- ')*(len(field_card_name)))
    print(('-'+'Strenght:'.center(11)+'- ')*(len(field_card_name)))

    for i in range(len(field_card_str)):
        print('-'+str(field_card_str[i]).center(11)+'- ', end='')

    print('\n'+('-'+' '*11+'- ')*(len(field_card_name)))
    print(('-'+'Crd num:'.center(11)+'- ')*(len(field_card_name)))
    
    for i in range(len(field_card_name)):
        print('-'+f'{i+1}'.center(11)+'- ', end='')
        
    print('\n'+('-'*13+' ')*(len(field_card_name)))
    
def show_cards_in_hand(hand):
    name = None
    if start_player == 0 and start_value == 2:
        name = 'Player 2:'
    elif start_player == 1 and start_value == 2:
        name = 'Player 1:'
    elif start_player == 1 and start_value == 1:
        name = 'Player'
    print(f'Cards in your hand - {name}')
    
    print(('-'*13+' ')*(len(hand)))

    for i in range(len(hand)):
        if hand[i]==11:
            print('-'+'Jack'.center(11)+'- ', end='')
        elif hand[i]==12:
            print('-'+'Queen'.center(11)+'- ', end='')
        elif hand[i]==13:
            print('-'+'King'.center(11)+'- ', end='')
        elif hand[i]==14:
            print('-'+'Ace'.center(11)+'- ', end='')
        elif hand[i]==15:
            print('-'+'Joker'.center(11)+'- ', end='')
        else:    
            print('-'+str(hand[i]).center(11)+'- ', end='')

    print('\n'+('-'+' '*11+'- ')*(len(hand)))
    print(('-'+'Strenght:'.center(11)+'- ')*(len(hand)))

    for i in range(len(hand)):
        print('-'+str(hand[i]).center(11)+'- ', end='')
    
    print('\n'+('-'+' '*11+'- ')*(len(hand)))
    print(('-'+'Crd num:'.center(11)+'- ')*(len(hand)))
    
    for i in range(len(hand)):
        print('-'+f'{i+1}'.center(11)+'- ', end='')
        
    print('\n'+('-'*13+' ')*(len(hand)))
    
    
def choose_card_to_attack(your_field, enemy_field, enemy_field_name):
    if len(your_field) != 1:
        choosen_card = enter_value('Which card you want attack your enemy? Choose number: ',
                                   'You may enter only numbers from 1 to '
                                   f'{len(your_field)}', int, len(your_field), 0)
    else:
        choosen_card = enter_value('Which card you want attack your enemy? Choose number: ',
                                   'You may enter only number '
                                   f'{len(your_field)}', int, len(your_field), 0)
    if len(enemy_field) != 1:     
        attacked_card = enter_value('Which card you want attack from field of you enemy? '
                                    'Choose number ', 'You may enter only numbers from 1 to '
                                    f'{len(enemy_field)}', int, len(enemy_field), 0)
    else:
        attacked_card = enter_value('Which card you want attack from field of you enemy? '
                                    'Choose number ', 'You may enter only number '
                                    f'{len(enemy_field)}', int, len(enemy_field), 0)
                                    
    enemy_field[attacked_card-1]-=your_field[choosen_card-1]
    if enemy_field[attacked_card-1] <= 0:
        enemy_field.remove(enemy_field[attacked_card-1])
        enemy_field_name.remove(enemy_field_name[attacked_card-1])
   
def choose_card_to_field(hand):
    choosen_card = enter_value('Which card you want send to field? Choose number: ',
                               'You may enter only numbers from 1 to '
                               f'{len(hand)}', int, len(hand), 0)
    return choosen_card 


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cards_basic = [2, 3, 4, 5, 6, 7, 8, 9, 
               10, 11, 12, 13, 14, 15]
   
deck_pOne = []+cards_basic
deck_pTwo = []+cards_basic
shuffle(deck_pOne)
shuffle(deck_pTwo)
field_pOne = []
field_pTwo = []
field_card_name_pOne = []
field_card_name_pTwo = []
hand_pOne = []
hand_pTwo = []
number_to_guess = randint(1, 10)
clear_terminal()
moves = 0

start_value = enter_value('Choose number from 1 to 3.\n1 -'+
 ' play with PC; 2 - play with other player; 3 - quit game. ',
'Incorrect value - choose only numbers from 1 to 3.', int, 3, 0)

if start_value==1 or start_value==2:
    
    start_player = start_minigame(start_value)
    
    add_cards_from_deck_to_hand(hand_pOne, deck_pOne, 1)
    add_cards_from_deck_to_hand(hand_pTwo, deck_pTwo, 1)
    
    if start_value==2:
        while( (len(deck_pOne) or len(hand_pOne) or len(field_card_name_pOne)) != 0 and
               (len(deck_pTwo) or len(hand_pTwo) or len(field_card_name_pTwo)) != 0):
                   
            if start_player==1:
                print(f'Cards in your deck Player 1: {len(deck_pOne)}\n')

                if moves>=1:
                    print('Cards in your enemy field:')
                    show_card_in_field(field_card_name_pTwo, field_pTwo)
                    
                if (moves>1 and len(field_pOne)>0):
                    print('Cards in your field - Player 1:')
                    show_card_in_field(field_card_name_pOne, field_pOne)
                    
                if (len(deck_pOne)!=0 and len(hand_pOne)<=4):  
                    add_cards_from_deck_to_hand(hand_pOne, deck_pOne, 1)
                
                if len(hand_pOne)!=0:
                    show_cards_in_hand(hand_pOne)
                
                if (len(field_card_name_pOne)<=4 and len(hand_pOne)!=0):
                    choosen_card = choose_card_to_field(hand_pOne)
                    add_cards_from_hand_to_field(field_card_name_pOne, field_pOne, hand_pOne, choosen_card)
                 
                clear_terminal()

                if moves>1:
                    print('Cards in your enemy field:')
                    show_card_in_field(field_card_name_pTwo, field_pTwo)
                    print('Cards in your field - Player 1:')
                    show_card_in_field(field_card_name_pOne, field_pOne)
                    
                    choose_card_to_attack(field_pOne, field_pTwo, field_card_name_pTwo)
                    
                
                start_player-=1 # -1 to 0 for move p2
                moves+=1
                
            elif start_player==0:
                print(f'Cards in your deck Player 2: {len(deck_pTwo)}\n')

                if moves>=1:
                    print('Cards in your enemy field:')
                    show_card_in_field(field_card_name_pOne, field_pOne)
                    
                if (moves>1 and len(field_pTwo)>0):
                    print('Cards in your field - Player 2:')
                    show_card_in_field(field_card_name_pTwo, field_pTwo)
               
                if (len(deck_pTwo)!=0 and len(hand_pTwo)<=4):               
                    add_cards_from_deck_to_hand(hand_pTwo, deck_pTwo, 1)
                    
                if len(hand_pTwo)!=0:
                    show_cards_in_hand(hand_pTwo)
                
                if (len(field_card_name_pTwo)<=4 and len(hand_pTwo)!=0):
                    choosen_card = choose_card_to_field(hand_pTwo)
                    add_cards_from_hand_to_field(field_card_name_pTwo, field_pTwo, hand_pTwo, choosen_card)
                    
                clear_terminal()

                if moves>1:
                    print('Cards in your enemy field')
                    show_card_in_field(field_card_name_pOne, field_pOne)
                    print('Cards in your field - Player 2:')
                    show_card_in_field(field_card_name_pTwo, field_pTwo)
                    
                    choose_card_to_attack(field_pTwo, field_pOne, field_card_name_pOne)               
                
                start_player+=1 # +1 to 1 for move p1
                moves+=1

        if len(deck_pOne) == 0 and len(hand_pOne) == 0 and len(field_card_name_pOne) == 0:
            print('Winner is Player 2')
        elif len(deck_pTwo) == 0 and len(hand_pTwo) == 0 and len(field_card_name_pTwo) == 0:
            print('Winner is Player 1')
        
elif start_value==3:
    print('Game exit...')
    quit()
