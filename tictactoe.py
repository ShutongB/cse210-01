"""
Tic-Tac-Toe
Shutong Bao
"""

# create board function


def create_board():
    board = []
    for slot in range(9):
        board.append(slot + 1)
    return board

# print board function


def print_board(board):
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('- + - + -')
    print(board[3], '|', board[4], '|', board[5])
    print('- + - + -')
    print(board[6], '|', board[7], '|', board[8])
    print()


turn_count = 0


def turn(turn_count):
    # while turn is odd, player is X
    # while turn is even, player is O
    if turn_count % 2 == 0:
        return "O"
    else:
        return "X"


def player_turn(player, board):
    if player == "X":
        spot = int(input("Choose a spot (1-9): "))
        while spot not in range(1, 10):
            spot = int(
                input("You chose a number that is not between 1 and 9. Try again: "))
        while board[spot - 1] == "X" or board[spot - 1] == "O":
            spot = int(
                input("You chose a spot that is already taken from another player. Try again: "))
        board[spot - 1] = player
        print_board(board)
    else:
        spot = int(input("Choose a spot (1-9): "))
        while spot not in range(1, 10):
            spot = int(
                input("You chose a number that is not between 1 and 9. Try again: "))
        while board[spot - 1] == "X" or board[spot - 1] == "O":
            spot = int(
                input("You chose a spot that is already taken from another player. Try again: "))
        board[spot - 1] = player
        print_board(board)

# check if there is a winner


def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# check if there is a draw


def has_draw(board):
    # if all piece are taken and there is no winner, it is a draw
    count = 0
    for square in board:
        if square == 'X' or square == 'O':
            count += 1
        else:
            return False
    if count == 9:
        return True


def main(turn_count):
    board = create_board()
    print_board(board)
    while not has_winner(board) or has_draw(board):
        turn_count += 1
        if has_draw(board) == True:
            print("It's a draw!")
            break
        player_turn(turn(turn_count), board)
        if has_winner(board):
            print(turn(turn_count), "wins!")
            break


if __name__ == "__main__":
    main(turn_count)
