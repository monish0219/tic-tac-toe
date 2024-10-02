import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define global variables
current_player = "X"
buttons = []

# Function to check for a winner
def check_winner():
    # Winning combinations (rows, columns, diagonals)
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                  (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                  (0, 4, 8), (2, 4, 6)]            # Diagonals
    
    for combo in win_combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"]) and buttons[combo[0]]["text"] != "":
            return buttons[combo[0]]["text"]
    
    return None

# Function to handle button clicks
def on_button_click(index):
    global current_player
    
    # Prevent overwriting of already clicked button
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        
        # Check for a winner
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch turns
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button["text"] = ""

# Create the grid of buttons
for i in range(9):
    button = tk.Button(root, text="", font=('normal', 40), width=5, height=2, 
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the application
root.mainloop()
