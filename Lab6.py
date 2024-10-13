# Lab 6 - Connect 4
def initialize_board(num_rows, num_cols):
    board = []
    for row in range(num_rows):
        row = []
        for col in range(num_cols):
            row.append('-')
        board.append(row)
    return board

def print_board(board):
    board = reversed(board)
    for row in board:
        print(*row, sep=' ')

def insert_chip(board, col, chip_type):
    for row in board:
        if row[col] == '-':
            row[col] = chip_type
            print_board(board)
            return row

def check_if_winner(board, col, row, chip_type):
    count = 0
    for r in range(len(board)):
        if board[r][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    for r in range(len(board)):
        count = 0
        for c in range(len(board[0])):
            if board[r][c] == chip_type:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

def main():
    height = int(input("What would you like the height of the board to be?"))
    length = int(input("What would you like the length of the board to be?"))
    board0 = initialize_board(height, length)
    print_board(board0)
    print('\nPlayer 1: x')
    print('Player 2: o')
    while True:
        try:
            choice1 = int(input("\nPlayer 1: Which column would you like to choose?"))
        except EOFError:
            print("No input received. Exiting the game.")
            return
        insert_chip(board0, choice1, 'x')
        if check_if_winner(board0, choice1, height-1, 'x'):
            print("\nPlayer 1 won the game!")
            break
        if is_board_full(board0):
            print("\nDraw. Nobody wins.")
            return

        try:
            choice2 = int(input("\nPlayer 2: Which column would you like to choose?"))
        except EOFError:
            print("No input received. Exiting the game.")
            return
        insert_chip(board0, choice2, 'o')
        if check_if_winner(board0, choice2, height - 1, 'o'):
            print("\nPlayer 2 won the game!")
            break
        if is_board_full(board0):
            print("Draw. Nobody wins.")
            return


if __name__ == '__main__':
    main()
