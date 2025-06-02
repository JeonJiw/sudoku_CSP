# 🧩 Sudoku CSP Solver with MRV and Least Constraining Value

Jiwon Jeon

This is a Python project that solves Sudoku puzzles using **Constraint Satisfaction Problem (CSP)** strategies and **backtracking search**, enhanced with:

- 🧠 **MRV (Minimum Remaining Values)** for smart variable selection
- 🧩 **Least Constraining Value** for intelligent value ordering

You can choose a puzzle manually or let the program pick one randomly. After solving, you're prompted to solve another.

## 📂 Project Structure

```
sudoku_CSP/
├── sudoku_csp/
│   ├── main.py          # User interface and control flow
│   ├── solver.py        # CSP-based Sudoku solving logic (MRV + LCV)
│   └── puzzles.json     # List of puzzles to solve
|__ README.md
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

```
python main.py
```

---

## 🧠 Algorithms Used

### ✅ MRV (Minimum Remaining Values)

Selects the variable (empty cell) with the fewest remaining legal values, allowing the solver to "fail fast" and reduce unnecessary search.

### ✅ Least Constraining Value (LCV)

For a given cell, values are tried in an order that **constrains other cells the least**, preserving more options for future assignments.

These techniques combined significantly improve performance over basic backtracking.

## 📘 Sample Usage

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

---

## 🔧 Features

- Backtracking CSP solver
- MRV + LCV heuristics
- Pretty printed board
- Option to solve multiple puzzles interactively

---

## 📝 Future Improvements

- Add Forward Checking or AC-3 for arc consistency
- Support for loading user-uploaded puzzles
- GUI with Tkinter or Pygame

---

👤 Created by [Your Name]
🔗 Powered by Python CSP techniques
