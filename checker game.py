def initialize_board(boards)->str:
    '''
    Return the list of boards
    >>>initialize_board ["1111","1111","1111","0000","0000","2222","2222,"2222"]
    b
    '''
    for b ==initialize_board:
        return b
    

def display_board(gameboard)->list:
    '''
    Return the gameboard in correct order
    >>> display_board(gameboard)
    ['0','1','0','1','0','1','0','1']
    ['1','0','1','0','1','0','1','0']
    ['0','1','0','1','0','1','0','1']
    ['0','0','0','0','0','0','0','0']
    ['0','0','0','0','0','0','0','0']
    ['2','0','2','0','2','0','2','0']
    ['0','2','0','2','0','2','0','2']
    ['2','0','2','0','2','0','2','0']
    '''
    for i in gameboard:
        gameboard=b:
            print display_board(b)
    return  diaplay_board


def valid_piece (board,piece)->bool:
    '''
    Return Ture if the piece is valid
    >>>valid_piece (b,'21')
    True
    >>>valid_piece(b,'1111')
    False
    '''
    rows='r'
    columns='c'
    for i in piece:
        i='r'+'c':
            if range('r') and range('c')<=7
    return True
    else
    return False


def valid_move (board,move,piece)->bool:
    '''
    Return True iff moving the token at position piece
    >>>b=initialize_board
    >>>valid_move (b,'41','50')
    True
    >>>valid_move (b,'51','61')
    False
    '''
    rows=r
    columns=c
    while i in move:
        if i==piece:
            return False
           if piece=='0' or move=='0':
               return False
            if i='r'+'c':
                 i=('r'+num) +'c'or i='r'+('c'+num):
                     return False
                   for i==move and i==valid_piece:\
                       return False
                   else
    return True
    

def update_board(board: list, move: str, piece: str, player: int)-> bool:
    '''
    Update board by moving piece to move. Return True iff the opposing player has no valid moves after updating the game.

    '''

    if player != '1' and Player != '2':
        update.board(choose a player)

    if valid_move'1':
        return valid_move'2':
            return valid_move'1'
    
      




def update_player(player)-> int:
    '''
    Return player and other player as 1 and 2
    >>>update_player(player)
    1
    >>>Update_player(otherplayer)
    2
    '''
    if player == 1:
        otherplayer=2
    

if __name__ == "__main__":
    board = initilaize_board()
    player = 1
    gameover = False
    while not gameover:
        print(display_board(board))
        piece = input("Player {}, which piece would you like to move?".format(player))
        while not valid_piece(board, piece):
            piece = input("Player {}, pick a valid piece".format(player))
        move = input("Player {}, where would you like to move the piece at {}?".format(player, piece))
        while not valid_move(board, move, piece):
            move = input("Player {}, pick a valid move for the piece at {}.".format(player, piece))
        gameover = update_board(board, move, piece, player)
        player = update_player(player)
    player = update_player(player)
    print("Game over, player {} wins!".format(player))





    
    e
