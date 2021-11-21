import numpy as np

board = np.array( [['.', '.', '.'],
                   ['.', '.', '.'],
                   ['.', '.', '.']] )

game_status = True
player_one = True

def play():
    global player_one
    card = input('Enter row and column position')
    card = card.split(',')
    row = int(card[0])
    column = int(card[1])
    print(row, column)
    print(player_one)
    if player_one:
        if check_card( row, column ):
            if check_down( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins down x' )
                game_status = False
                return
            elif check_x( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins hor x' )
                game_status = False
                return
            elif check_diagonal( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins dig x' )
                game_status = False
                return
            elif check_raw( row, column, 'X' ) == 'endgame':
                print( 'End of the game play another one' )
                game_status = False
                return
            else:
                print(board)
                player_one = False
        else:
            print( 'Space taken.Choose another space' )
            player_one = False
    else:
        if check_card( row, column ):
            if check_down( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins down y' )
                game_status = False
                return
            elif check_x( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins hor y' )
                game_status = False
                return
            elif check_diagonal( row, column, 'X' ) == 'Win':
                print( 'Player 1 wins dig y' )
                game_status = False
                return
            elif check_raw( row, column, 'O' ) == 'endgame':
                print( 'End of the game play another one' )
                game_status = False
                return
            else:
                print(board)
            player_one = True
        else:
            print( 'Space taken.Choose another space' )
            player_one = True


def check_card(row, column):
    if board[row][column] == '.':
        return True
    else:
        return False

def check_down(row, column, value):
    if (
            (value == board[1][0] and value == board[2][0]) or
            (value == board[0][0] and value == board[2][0]) or
            (value == board[1][0] and value == board[0][0]) or
            (value == board[1][1] and value == board[2][1]) or
            (value == board[0][1] and value == board[2][1]) or
            (value == board[0][1] and value == board[1][1]) or
            (value == board[1][2] and value == board[2][2]) or
            (value == board[0][2] and value == board[2][2]) or
            (value == board[0][2] and value == board[1][2])
    ):
        board[row][column] = value
        print( board )
        return 'Win'
    else:
        'no'


def check_x(row, column, value):
    if (
            ((value == board[0][1]) and value == board[0][2]) or
            (value == board[0][0] and value == board[0][2]) or
            (value == board[0][0] and value == board[0][1]) or
            (value == board[1][1] and value == board[1][2]) or
            (value == board[1][0] and value == board[1][2]) or
            (value == board[1][0] and value == board[1][1]) or
            (value == board[2][1] and value == board[2][2]) or
            (value == board[2][0] and value == board[2][2]) or
            (value == board[2][0] and value == board[2][1])
    ):
        board[row][column] = value
        print( board )
        return 'Win'
    else:
        'no'


def check_diagonal(row, column, value):
    if ( (value == board[1][1] and value  == board[2][2] ) or
            (value == board[0][0] and value == board[2][2]) or
            (value == board[0][0] and value == board[1][1]) or
            (value == board[1][1] and value == board[0][2]) or
            (value == board[2][0] and value == board[0][2]) or
            (value == board[2][0] and value == board[0][2]) ):
        board[row][column] = value
        print( board )
        return 'Win'
    else:
        'no'


def check_raw(row, column, value):
    board[row][column] = value
    free_space_counter = 0
    for i in range( 3 ):
        for x in range( 3 ):
            if board[i][x] == '.':
                free_space_counter += 1;
    if free_space_counter == 0:
        return 'endgame'

while game_status:
    play()

