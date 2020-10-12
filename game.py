# intro
print("Welcome to Checkers, the best game ever")
player1_name = input("Enter player1 name: ")
player2_name = input("Enter player2 name: ")

# define empty board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(b):
    """ Function to display the board """
    for row in b:
        print(row)


def who_won(b):
    """ Check if the game is finished
        returns "X" if player1 won
        returns "O" if player2 won
        returns " " if game is not over
    """

    def check_row(x_or_o):
        return any(
            [
                row[0] == x_or_o and row[1] == x_or_o and row[2] == x_or_o
                for row in b
            ]
        )

    # Check if there is a row of x's
    x_row = check_row("X")
    # Check if there is a row of o's
    o_row = check_row("O")

    def check_column(x_or_o):
        return any(
            [
                all([row[column] == x_or_o for row in b])
                for column in range(0, 3)
            ]
        )

    # Check if there is a column of x's
    x_column = check_column("X")
    # Check if there is a column of o's
    o_column = check_column("O")

    if x_row or x_column:
        return "X"
    elif o_row or o_column:
        return "O"
    else:
        return " "


current_player = player2_name

# game loop
while who_won(board) == " ":
    print_board(board)
    print(f"{current_player}, it is your turn!")
    row = int(input("Pick a row between 0 and 2: "))
    column = int(input("Pick a column between 0 and 2: "))
    if board[row][column] == " ":
        board[row][column] = "X" if current_player == player1_name else "O"
        current_player = (
            player1_name if current_player == player2_name else player2_name
        )

if who_won(board) == "X":
    winning_player = player1_name
else:
    winning_player = player2_name
print(f"Congratulations {winning_player}, you have won!")
