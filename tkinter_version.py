"""
tkinter_version.py - Jeu Tic-Tac-Toe avec interface Tkinter
"""

import tkinter as tk
from tkinter import messagebox, font
from game_logic import TicTacToe

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe - Version Tkinter")
        self.root.configure(bg='#2c3e50')
        
        
        self.game = TicTacToe()
        
        
        self.button_font = font.Font(family='Helvetica', size=24, weight='bold')
        self.title_font = font.Font(family='Helvetica', size=20, weight='bold')
        self.status_font = font.Font(family='Helvetica', size=14)
        
       
        self.main_frame = tk.Frame(root, bg='#2c3e50', padx=20, pady=20)
        self.main_frame.pack(expand=True)
        
       
        self.title_label = tk.Label(
            self.main_frame, 
            text="🎮 TIC-TAC-TOE 🎮", 
            font=self.title_font, 
            fg='#ecf0f1', 
            bg='#2c3e50'
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
      
        self.status_label = tk.Label(
            self.main_frame, 
            text="Tour du joueur: X", 
            font=self.status_font, 
            fg='#f1c40f', 
            bg='#2c3e50'
        )
        self.status_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(
                    self.main_frame,
                    text='', 
                    font=self.button_font,
                    width=4, 
                    height=2,
                    bg='#34495e',
                    fg='#ecf0f1',
                    activebackground='#1abc9c',
                    activeforeground='#ffffff',
                    relief='raised',
                    borderwidth=3,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                button.grid(row=i+2, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
      
        self.control_frame = tk.Frame(self.main_frame, bg='#2c3e50')
        self.control_frame.grid(row=5, column=0, columnspan=3, pady=(20, 0))
        
        
        self.reset_button = tk.Button(
            self.control_frame,
            text="Nouvelle Partie", 
            font=self.status_font,
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            width=15,
            command=self.reset_game
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
       
        self.quit_button = tk.Button(
            self.control_frame,
            text="Quitter", 
            font=self.status_font,
            bg='#7f8c8d',
            fg='white',
            activebackground='#95a5a6',
            width=10,
            command=root.quit
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
    
    def on_button_click(self, row, col):
        """Gère le clic sur un bouton du plateau"""
        if self.game.make_move(row, col):
            
            self.buttons[row][col].config(
                text=self.game.board[row][col],
                fg='#1abc9c' if self.game.board[row][col] == 'X' else '#e74c3c',
                state='disabled'
            )
            
            
            if self.game.game_over:
                if self.game.winner:
                    messagebox.showinfo(
                        "Félicitations!", 
                        f"Le joueur {self.game.winner} a gagné!"
                    )
                else:
                    messagebox.showinfo("Match nul!", "Aucun gagnant!")
                self.disable_all_buttons()
            else:
                
                self.status_label.config(
                    text=f"Tour du joueur: {self.game.current_player}",
                    fg='#f1c40f' if self.game.current_player == 'X' else '#9b59b6'
                )
    
    def disable_all_buttons(self):
        """Désactive tous les boutons du plateau"""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')
    
    def reset_game(self):
        """Réinitialise le jeu"""
        self.game.reset_game()
        
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text='',
                    state='normal',
                    fg='#ecf0f1'
                )
        
        
        self.status_label.config(
            text="Tour du joueur: X",
            fg='#f1c40f'
        )

def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()