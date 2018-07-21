print('Welcome to Tic Tac Toe!')
player_one = input('Player 1: Do you want to be X or O? ')

while player_one.lower() != 'x' and player_one.lower() != 'o':
    player_one = input('Please choose X or O : ')
    
if player_one.lower() == 'x':
    player_two = 'O'
    player_one = 'X'
elif player_one.lower() == 'o':
    player_one = 'O'
    player_two = 'X'

permission = input('\nAre you ready to play? Enter yes or no ')
while permission.lower() != 'yes' and permission.lower() != 'no':
    permission = input('Please input yes or no ')    


def display_board(display):
    '''
    Displays the board
    '''
    print('\n'*16)
    print('        ', '|', '        ', '|', '        ')
    print('   {}    '.format(display[0]), '|', '   {}    '.format(display[1]), '|', '   {}    '.format(display[2]))
    print('        ', '|', '        ', '|', '        ')
    print('-----------------------------')
    print('        ', '|', '        ', '|', '        ')
    print('   {}    '.format(display[3]), '|', '   {}    '.format(display[4]), '|', '   {}    '.format(display[5]))
    print('        ', '|', '        ', '|', '        ')
    print('-----------------------------')  
    print('        ', '|', '        ', '|', '        ')
    print('   {}    '.format(display[6]), '|', '   {}    '.format(display[7]), '|', '   {}    '.format(display[8]))
    print('        ', '|', '        ', '|', '        ')
    print('\n'*10)

def game_won(board, player):
    '''
    Determines if the game has been won by looking at the combination of plays on the list
    '''

    # Account for the fact that the index starts form zero

    return ((board[0] == board[1] == board[2] == player) or
    (board[3] == board[4] == board[5] == player) or
    (board[6] == board[7] == board[8] == player) or
    (board[0] == board[3] == board[6] == player) or
    (board[1] == board[4] == board[7] == player) or
    (board[2] == board[5] == board[8] == player) or
    (board[0] == board[4] == board[8] == player) or
    (board[2] == board[4] == board[6] == player))

is_player_one = True

def det_player():
    '''
    Function that determines which player is to play
    To be used with get_input fuction
    '''
    global is_player_one
    if is_player_one == True:
        is_player_one = False
        return 'player one'
    elif is_player_one == False:
        is_player_one = True
        return 'player two'

def get_input(avail_positions):
    '''
    Get's the player input
    '''
    which_player = det_player()
    allowed = [1,2,3, 4, 5, 6, 7, 8, 9]

    if which_player == 'player one':
        player_one_input = int(input('Player One: Choose your next position (1-9) '))
        while player_one_input not in allowed or player_one_input not in avail_positions:
            if player_one_input not in allowed:
                player_one_input = int(input('Player One: PLEASE!!! Choose a number between one and nine '))
            elif player_one_input not in avail_positions:
                player_one_input = int(input('Player One: Sorry Position taken '))
        return player_one_input, 'player one'

    elif which_player == 'player two':
        player_two_input = int(input('Player Two: Choose your next position (1-9) '))
        while player_two_input not in allowed or player_two_input not in avail_positions:
            if player_two_input not in allowed:
                player_two_input = int(input('Player Two: PLEASE!!! Choose a number between one and nine '))
            elif player_two_input not in avail_positions:
                player_two_input = int(input('Player Two: Sorry Position taken '))
        return player_two_input, 'player two'

def replay():
    '''
    Asks the player if they want to play again
    '''

    global is_player_one
    replay_ques = input('\nDo you want to play again? Enter yes or no ')
    while replay_ques.lower() != 'yes' and replay_ques.lower() != 'no':
        replay_ques = input('Please input yes or no ')
    if replay_ques == 'yes':
        is_player_one = True   # Makes it player one's turn
        return True

def game():
    # Setting default values
    values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    avail_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Displays the board initially
    display_board(values)

    #Initailize the game
    while True:
        # Get's the player's position and removes it from available positions
        position, player = get_input(avail_positions)
        avail_positions.remove(position)

        # Assigns variables on the board based on the received position
        if player == 'player one':
            values[position - 1] = player_one
        elif player == 'player two':
            values[position - 1] = player_two

        # Checks if the game has been won or drawn
        if len(avail_positions) <= 4:
            if game_won(values, player_one):
                display_board(values)
                print('Player One Won!!!')
                break
            elif game_won(values, player_two):
                display_board(values)
                print('Player Two Won!!!')
                break
        if len(avail_positions) < 1:
            print('DRAWWWW!!!')
            values = [' '*9]
            break
        
        # Displays the board while in the loop
        display_board(values)

# Asks before starting the game, and asks if to continue the game
if permission.lower() == 'yes':
    while True:
        game()
        if not replay():
            break