import tkinter as tk
from tkinter import messagebox

# --------- SUDOKU PUZZLE (0 = empty cell for user to solve) ----------
puzzle = [
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

# --------- CORRECT SOLUTION ----------
solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

window = tk.Tk()
window.title("Sudoku Game")

entries = [[None for _ in range(9)] for _ in range(9)]

# --------- CREATE 3×3 FRAMES WITH BORDERS ---------
frames = [[None for _ in range(3)] for _ in range(3)]

for br in range(3):
    for bc in range(3):
        frame = tk.Frame(window, bd=3, relief="solid")  # solid black border
        frame.grid(row=br, column=bc, padx=2, pady=2)
        frames[br][bc] = frame

# --------- PLACE CELLS INSIDE THEIR 3×3 FRAMES ---------
for r in range(9):
    for c in range(9):
        frame = frames[r // 3][c // 3]  # pick correct 3×3 frame

        e = tk.Entry(frame, width=3, font=("Arial", 18), justify="center")

        e.grid(row=r % 3, column=c % 3, padx=1, pady=1)

        if puzzle[r][c] != 0:
            e.insert(0, puzzle[r][c])
            e.config(state="disabled", disabledforeground="green")

        entries[r][c] = e


# --------- CHECK FUNCTION ---------
def check_solution():
    for r in range(9):
        for c in range(9):
            val = entries[r][c].get()

            if val == "":
                messagebox.showerror("Error", "Please fill all cells!")
                return

            if not val.isdigit() or not (1 <= int(val) <= 9):
                messagebox.showerror("Error", "All cells must be numbers 1–9!")
                return

            if int(val) != solution[r][c]:
                messagebox.showerror("Incorrect", "❌ Wrong solution! Try again.")
                return

    messagebox.showinfo("Correct", "🎉 Congratulations! You solved the puzzle!")


# --------- CHECK BUTTON ---------
btn = tk.Button(window, text="CHECK PUZZLE", font=("Arial", 16),
                bg="green", fg="white", command=check_solution)
btn.grid(row=3, column=0, columnspan=3, sticky="nsew")  # below the 3x3 block rows

window.mainloop()