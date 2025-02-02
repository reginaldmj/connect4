# Initialize a 7-column, 6-row Connect Four board
board = [[' ' for _ in range(7)] for _ in range(6)]

# Function to print the board with column labels and row separators
def print_board(board):
    # Print the column labels
    print(" 1   2   3   4   5   6   7")
    # Print each row with separators
    for row in board:
      print("+---+---+---+---+---+---+---+")
      print("|", " | ".join(row), "|")
      

# Function to drop a piece into a column
def drop_piece(board, column, player):
    # Make sure the column number is valid (1 through 7)
    if column < 1 or column > 7:
        print("Invalid column. Choose a column between 1 and 7.")
        return False
    
    # Check if the column is full
    for row in range(5, -1, -1):
        if board[row][column - 1] == ' ':
            board[row][column - 1] = player
            return True
    
    # If no empty spaces, return False
    print("Column is full. Try a different one.")
    return False

# Example of gameplay
# print_board(board)
# drop_piece(board, 3, 'X')  # Player 'X' drops a piece in column 3
# print_board(board)
# drop_piece(board, 4, 'O')  # Player 'O' drops a piece in column 4
# print_board(board)