import csv
import numpy as np
from sudoku import Sudoku

def generate_sudoku_dataset(filename="sudokus.csv", num_difficulties=10, boards_per_diff=10):
    difficulties = np.linspace(0.5, 0.85, 10)
    print(difficulties)
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["difficulty", "board"])
        
        for diff in difficulties:
            for _ in range(boards_per_diff):
                puzzle = Sudoku(3, 3).difficulty(diff)
                board = puzzle.board
                
                board_str = "".join(
                    str(cell) if cell is not None else "."
                    for row in board
                    for cell in row
                )
                
                writer.writerow([diff, board_str])
                
    print(f"Generated {num_difficulties * boards_per_diff} boards and saved to {filename}")


if __name__ == "__main__":
    generate_sudoku_dataset()