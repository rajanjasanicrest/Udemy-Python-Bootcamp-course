def check_result(matrix):
    if matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X' or  matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X' or matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X' or matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X' or matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X' or matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X' or matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X' or matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X':
        return 1
    
    elif matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O' or matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O' or matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O' or matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O' or matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O' or matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O' or matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O' or matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O':
        return 2
    
    else:
        return 0

def print_board(matrix):    
    print(matrix)
    print(f'     |     |     ')
    print(f'  {matrix[0][0]}  |  {matrix[0][1]}  | {matrix[0][2]}  ')
    print(f'     |     |     ')
    print('-------------------')
    print(f'     |     |     ')
    print(f'  {matrix[1][0]}  |  {matrix[1][1]}  | {matrix[1][2]}  ')
    print(f'     |     |     ')
    print('-------------------')
    print(f'     |     |     ')
    print(f'  {matrix[2][0]}  |  {matrix[2][1]}  | {matrix[2][2]}  ')
    print(f'     |     |     ')

def place_move(matrix, move, character):
    if move == 1 or move == 2 or move == 3:
        matrix[0][move-1] = character
    elif move == 4 or move == 5 or move == 6:
        matrix[1][move-4] = character
    elif move == 7 or move == 8 or move == 9:
        matrix[2][move-7] = character
    
    return matrix
    
def start_game(): 
    winner = ""
    print("Hello Players, Please note the below board positions and use those position numbers to make your move")
    print(f'     |     |     ')
    print(f'  1  |  2  |  3  ')
    print(f'     |     |     ')
    print('-------------------')
    print(f'     |     |     ')
    print(f'  4  |  5  |  6  ')
    print(f'     |     |     ')
    print('-------------------')
    print(f'     |     |     ')
    print(f'  7  |  8  |  9  ')
    print(f'     |     |     ')
    player1 = input("Enter Name of Player 1: ")
    player2 = input("Enter Name of Player 2: ")
    print(f"{player1} plays as X and {player2} as O ")
    matrix = [ [' ' for _ in range(3)] for _ in range(3)] 
    
    print_board(matrix)
    already_entered = []
    curr_move = 0
    while curr_move != 9:
        if curr_move % 2 == 0:
            move = 0
            while move not in range(1,10):
                move = int(input(f"{player1}'s Turn: Please select square to put your character (1-9) : "))
                if move in already_entered:
                    move = 0
                    print("You cannot repeat the move!")
                    continue
                if move > 9 and move <= 0:
                    print("Invalid Move : Choose between 1 - 9")
            matrix = place_move(matrix, move, 'X' )
            already_entered.append(move)

        else:
            move = 0
            while move not in range(1,10):
                move = int(input(f"{player2}'s Turn: Please select square to put your character (1-9) : "))
                if move in already_entered:
                    move = 0
                    print("You cannot repeat the move")
                    continue
                if move > 9 or move <= 0:
                    print("Invalid Move : Choose between 1 - 9")
            matrix = place_move(matrix, move, 'O' )
            already_entered.append(move)

        print_board(matrix)
        tw = check_result(matrix) 
        if tw == 1 or tw == 2:
            break
        
        curr_move += 1
    
    tw = check_result(matrix)
    if tw == 1:
        return player1
    elif tw == 2:
        return player2
    else:
        return 'D'

if __name__ == '__main__':
    opt = input("Do You want to play Tic Tac Toe? (Y/N) :")
    while opt not in 'nN':
        if opt in 'Yy':
            winner = start_game()
            if winner == 'D':
                print("The Game is Drawn! Please play again")
            else:
                print(f'Congratulations {winner}!! You have won the Game')
        opt = input("Do You want to play Tic Tac Toe? (Y/N) :")

    if opt in 'nN':
        print("Thanks for playing this game")

