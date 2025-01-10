# Sudoku Solver with Visualization

## Project Description
This project is a Python-based Sudoku solver that uses the **backtracking algorithm** and visualizes the solving process in real time using the `matplotlib` library. The program takes a partially filled Sudoku board as input and attempts to solve it while adhering to Sudoku rules.

---

## Features
- **Efficient Algorithm:** Utilizes the backtracking algorithm to solve the Sudoku puzzle.
- **Real-Time Visualization:** Shows the solving process dynamically, making it easier to understand how backtracking works.
- **User-Friendly Output:** Prints the initial and solved Sudoku boards in the console for reference.
- **Configurable Visualization Speed:** You can adjust the speed of the visualization by modifying a delay parameter.

---

## Technologies Used
- **Python**: The core programming language used for logic implementation.
- **Matplotlib**: A Python library for plotting the Sudoku board and visualizing the solving process.

---

## How It Works
1. **Input:**
   - The Sudoku board is represented as a 2D list where `0` indicates empty cells.
   - Example:
     ```python
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
     ```

2. **Algorithm:**
   - The program employs backtracking, a depth-first search technique, to explore all possible solutions. It places a number in an empty cell, validates it, and recursively proceeds to solve the rest of the board.

3. **Visualization:**
   - Each step of the algorithm updates the grid dynamically using `matplotlib`.

4. **Output:**
   - Prints the initial Sudoku board and the solved board to the console.
   - Displays the solving process in a pop-up visualization window.

---

## Setup and Installation

1. **Prerequisites:**
   - Python 3.x installed on your system.
   - `matplotlib` library.

2. **Install Dependencies:**
   Run the following command to install `matplotlib`:
   ```bash
   pip install matplotlib
   ```

3. **Download the Script:**
   Save the Python script (`sudoku_solver.py`) to your local machine.

4. **Run the Script:**
   Open your terminal, navigate to the directory where the script is saved, and execute:
   ```bash
   python sudoku_solver.py
   ```

---

## How to Use
1. Modify the `sudoku_board` variable in the script to represent your Sudoku puzzle.
2. Run the script to solve the puzzle.
3. Observe the solving process in the visualization window.
4. Check the solved Sudoku board printed in the console.

---

## Customization
- **Visualization Speed:**
   - Adjust the delay in the visualization by modifying the `time.sleep(0.2)` line in the `solve_sudoku` function.
   - Example: To make it faster, change it to:
     ```python
     time.sleep(0.05)
     ```

- **Board Input:**
   - Replace the `sudoku_board` variable with your own puzzle input.

---


## Limitations
- The script assumes the input Sudoku board has a valid solution.
- For extremely complex puzzles, the solving process may be slow.

---

## License
This project is open-source and available for use and modification.

---

## Acknowledgments
- Algorithm inspired by classic backtracking approaches to constraint satisfaction problems.
- Visualization made possible using the `matplotlib` library.

