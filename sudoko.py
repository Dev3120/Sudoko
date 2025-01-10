import matplotlib.pyplot as plt
import time

def is_valid(board, row, col, num):
    """
    Check if placing `num` at board[row][col] is valid.
    """
    for x in range(9):
        if board[row][x] == num:  # Check row
            return False
        if board[x][col] == num:  # Check column
            return False

    # Check 3x3 sub-grid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking and visualization.
    """
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # No empty cells, puzzle solved

    row, col = empty_cell

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(board, row, col, num):
            board[row][col] = num
            visualize_board(board)  # Visualize the board
            time.sleep(0.2)  # Pause for better visualization

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Undo placement (backtrack)

    return False


def find_empty(board):
    """
    Find the next empty cell in the board.
    Returns (row, col) or None if no empty cells.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def visualize_board(board):
    """
    Visualize the Sudoku board using matplotlib.
    """
    plt.clf()  # Clear the current plot
    plt.imshow([[1 if cell else 0 for cell in row] for row in board], cmap="cool", interpolation="nearest")

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                plt.text(j, i, str(board[i][j]), ha='center', va='center', fontsize=16, color='black')

    # Draw grid lines
    for i in range(1, 9):
        lw = 2 if i % 3 == 0 else 0.5
        plt.axhline(i - 0.5, color="black", linewidth=lw)
        plt.axvline(i - 0.5, color="black", linewidth=lw)

    plt.xticks([])
    plt.yticks([])
    plt.pause(0.01)  # Update the plot


def print_board(board):
    """
    Print the Sudoku board in a readable format.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


# Example Sudoku Board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Initial Sudoku Puzzle:")
print_board(sudoku_board)

plt.ion()  # Enable interactive mode for matplotlib
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists!")
plt.ioff()  # Disable interactive mode
plt.show()  # Show the final plot
