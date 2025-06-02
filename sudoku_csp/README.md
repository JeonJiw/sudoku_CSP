# 🧩 Sudoku CSP Solver

Jiwon Jeon

This is a Python project that solves Sudoku puzzles using Constraint Satisfaction Problem (CSP) techniques and backtracking search.

You can either:

- Select a puzzle manually
- Or let the program randomly choose one for you

After solving one puzzle, you'll be asked if you want to solve another.

## 📂 Project Structure

```
sudoku_CSP/
├── sudoku_csp/
│   ├── main.py          # Main solver code
│   └── puzzles.json     # Contains a list of Sudoku puzzles
```

## 🚀 How to Run

1. Make sure Python 3 is installed:

```
python –version
```

2. Navigate to the project directory:

```
cd sudoku_CSP/sudoku_csp
```

3. Run the program:

````
python main.py
```

## 🧠 Features

- Backtracking search with constraint checking
- Solves standard 9x9 Sudoku puzzles
- Supports both user-selected and random puzzle solving
- Automatically displays the solved board
- Offers option to solve more puzzles in a loop

## 📘 Sample Usage
````

🧩 Choose a puzzle:

1. Puzzle 1
2. Puzzle 2
3. Puzzle 3
4. Puzzle 4
5. Puzzle 5
6. Puzzle 6
7. Puzzle 7
8. Puzzle 8
9. Puzzle 9
10. Puzzle 10

Enter number (1–10) or press Enter for random: 3

🧩 Selected Puzzle:
. . . | . . . | . 1 2
…

✅ Solved Puzzle:
4 3 7 | 9 5 6 | 8 1 2
…

🔁 Would you like to solve another puzzle? (Y/N): y

```

```
