
# print('\n'*100)
def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

################################

def player_input():
    player = ''
    valid_input = False
    while valid_input != True:
        player = input("Please pick a marker 'X' or 'O'")
        if player == 'X' or player == 'O':
            valid_input = True
        else:
            print("Not an 'X' or an 'O'.  Please try again")
            
    mark = player
    return mark


################################

def place_marker(board, marker, position):
    position_int = int(position)
    board[position_int] = marker
    return board

################################

 def win_check(board, mark):
    #789  963  753  
    #456  852  951
    #123  741  
    if board[1]== mark and board[2]== mark and board[3]== mark:
        return True
    elif board[4]== mark and board[5]== mark and board[6]== mark:
        return True
    elif board[7]== mark and board[8]== mark and board[9]== mark:
        return True
    elif board[7]== mark and board[4]== mark and board[1]== mark:
        return True
    elif board[8]== mark and board[5]== mark and board[2]== mark:
        return True
    elif board[9]== mark and board[6]== mark and board[3]== mark:
        return True
    elif board[7]== mark and board[5]== mark and board[3]== mark:
        return True
    elif board[9]== mark and board[5]== mark and board[1]== mark:
        return True
    else:
        return False

################################

import random

def choose_first():
    first = random.randint(1,2)
    print("Player {} goes first!".format(first))

################################

def space_check(board, position):
    is_avail = False
    position_int = int(position)
    if board[position_int] == '*':
        is_avail = True
    return is_avail
        
    
 

################################


def full_board_check(board):
    full = False
    full_count = 0
    for i in board:
        if i == '*':
            continue
        elif i == 'X' or i == 'O':
            full_count += 1
    if full_count == 9:
        full = True
    return full

################################

def player_choice(board):
    position_input = input("Please pick a potion to place your marker (1-9)")
    if space_check(board, position_check) == True:
        return position_input
    else:
        return "Position is filled"

################################

def replay():
    again = input("Would you like to play again? Y/N")
    if again == 'Y' or again == 'N':
        return True
    else:
        return False

################################

print('Welcome to Tic Tac Toe!')
game_on = False
full_board = False

while True:
    
    start_board = ['#'] * 10
    display_board(start_board)
    choose_first()
    game_on = True
    pass
    
    while game_on == True:
        print("First player's turn")
        full_board = full_board_check(start_board)
        if full_board == True:
            print("Board is full! Draw!")
            game_on = False
            break
        marker = player_input()
        position = player_choice(start_board)
        place_marker(start_board, marker, position)
        if win_check(start_board, 'X') == True:
            game_on = False
            print("Player 1 has won!")
            break
        if win_check(start_board, 'O') == True:
            game_on = False
            print("Player 1 has won!")
            break
        display_board(start_board)
        
        print("Second player's turn")
        full_board = full_board_check(start_board)
        if full_board == True:
            print("Board is full! Draw!")
            game_on = False
            break
        marker = player_input()
        position = player_choice(start_board)
        place_marker(start_board, marker, position)
        if win_check(start_board, 'X') == True:
            game_on = False
            print("Player 2 has won!")
            break
        if win_check(start_board, 'O') == True:
            game_on = False
            print("Player 2 has won!")
            break
        display_board(start_board)
    
    if not replay():
        break











