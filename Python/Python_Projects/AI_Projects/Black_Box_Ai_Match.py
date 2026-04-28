import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Matching Game")
        self.root.geometry("400x450")
        
        # Game variables
        self.symbols = ["🍎", "🍌", "🍇", "🍓", "🍊", "🍑", "🥝", "🍒"] * 2  # 8 pairs
        random.shuffle(self.symbols)
        self.buttons = []
        self.flipped = []
        self.matched = []
        self.moves = 0
        
        # UI Elements
        self.moves_label = tk.Label(root, text="Moves: 0", font=("Arial", 14))
        self.moves_label.pack(pady=10)
        
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        # Create 4x4 grid of buttons
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.frame, text="", width=8, height=4, font=("Arial", 16),
                                command=lambda r=i, c=j: self.flip_card(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)
        
        self.restart_btn = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_btn.pack(pady=10)
    
    def flip_card(self, row, col):
        if (row, col) in self.flipped or (row, col) in self.matched:
            return
        
        btn = self.buttons[row][col]
        symbol = self.symbols[row * 4 + col]
        btn.config(text=symbol, state="disabled")
        self.flipped.append((row, col))
        
        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)  # Delay for visibility
    
    def check_match(self):
        pos1, pos2 = self.flipped
        symbol1 = self.symbols[pos1[0] * 4 + pos1[1]]
        symbol2 = self.symbols[pos2[0] * 4 + pos2[1]]
        
        if symbol1 == symbol2:
            self.matched.extend(self.flipped)
            self.buttons[pos1[0]][pos1[1]].config(bg="green")
            self.buttons[pos2[0]][pos2[1]].config(bg="green")
        else:
            self.buttons[pos1[0]][pos1[1]].config(text="", state="normal")
            self.buttons[pos2[0]][pos2[1]].config(text="", state="normal")
        
        self.flipped = []
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")
        
        if len(self.matched) == 16:  # All matched
            messagebox.showinfo("Congratulations!", f"You won in {self.moves} moves!")
    
    def restart_game(self):
        random.shuffle(self.symbols)
        self.flipped = []
        self.matched = []
        self.moves = 0
        self.moves_label.config(text="Moves: 0")
        
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].config(text="", state="normal", bg="SystemButtonFace")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
    