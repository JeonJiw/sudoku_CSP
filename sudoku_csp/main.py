import json
import random
from solver import solve_sudoku, print_board 

def load_puzzles(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def select_puzzle(puzzles):
    print("\n🧩 Choose a puzzle:")
    for i in range(len(puzzles)):
        print(f"{i + 1}. Puzzle {i + 1}")
    choice = input(f"Enter number (1-{len(puzzles)}) or press Enter for random: ")
    if choice.strip().isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(puzzles):
            return puzzles[idx]
    return random.choice(puzzles)


if __name__ == "__main__":
    puzzles = load_puzzles("puzzles.json")

    while True:
        sudoku_board = select_puzzle(puzzles)

        print("\n🧩 Selected Puzzle:")
        print_board(sudoku_board)

        board_copy = [row[:] for row in sudoku_board]  

        if solve_sudoku(board_copy):
            print("\n✅ Solved Puzzle:")
            print_board(board_copy)
        else:
            print("❌ No solution found.")

        again = input("\n🔁 Would you like to solve another puzzle? (Y/N): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye!")
            break