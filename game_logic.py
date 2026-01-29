"""
game_logic.py - Logique commune du jeu Tic-Tac-Toe
"""

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        self.move_count = 0
    
    def reset_game(self):
        """Réinitialise le jeu"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        self.move_count = 0
    
    def make_move(self, row, col):
        """
        Fait un mouvement sur le plateau
        Retourne True si le mouvement est valide, False sinon
        """
        if self.game_over or self.board[row][col] != ' ':
            return False
        
        self.board[row][col] = self.current_player
        self.move_count += 1
        
       
        if self.check_winner(row, col):
            self.winner = self.current_player
            self.game_over = True
        elif self.move_count == 9:
            
            self.game_over = True
        
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    
    def check_winner(self, row, col):
        """Vérifie s'il y a un gagnant après le dernier mouvement"""
        player = self.board[row][col]
        
       
        if all(self.board[row][c] == player for c in range(3)):
            return True
        
        
        if all(self.board[r][col] == player for r in range(3)):
            return True
        
        
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        
        
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def get_board_state(self):
        """Retourne une représentation textuelle du plateau"""
        board_str = ""
        for row in self.board:
            board_str += "|".join(row) + "\n"
            board_str += "-" * 5 + "\n"
        return board_str[:-6]  