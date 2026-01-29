"""
pygame_version.py - Jeu Tic-Tac-Toe avec interface Pygame
"""

import pygame
import sys
from game_logic import TicTacToe


pygame.init()


WIDTH, HEIGHT = 600, 700
CELL_SIZE = 150
MARGIN = 50
BOARD_SIZE = CELL_SIZE * 3


BACKGROUND = (44, 62, 80)
BOARD_COLOR = (52, 73, 94)
LINE_COLOR = (236, 240, 241)
X_COLOR = (26, 188, 156)  
O_COLOR = (231, 76, 60)   
TEXT_COLOR = (241, 196, 15)
BUTTON_COLOR = (46, 204, 113)
BUTTON_HOVER = (39, 174, 96)

class PygameTicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe - Version Pygame")
        self.clock = pygame.time.Clock()
        
        
        self.game = TicTacToe()
        
        
        self.title_font = pygame.font.SysFont('arial', 50, bold=True)
        self.status_font = pygame.font.SysFont('arial', 32)
        self.button_font = pygame.font.SysFont('arial', 28)
        
        
        self.board_x = (WIDTH - BOARD_SIZE) // 2
        self.board_y = MARGIN + 80
        
        
        self.reset_button = pygame.Rect(
            WIDTH // 2 - 100, 
            HEIGHT - 100, 
            200, 
            50
        )
    
    def draw_board(self):
        """Dessine le plateau de jeu"""
        
        board_rect = pygame.Rect(
            self.board_x - 10, 
            self.board_y - 10, 
            BOARD_SIZE + 20, 
            BOARD_SIZE + 20
        )
        pygame.draw.rect(self.screen, BOARD_COLOR, board_rect, border_radius=10)
        
       
        for i in range(1, 3):
            
            pygame.draw.line(
                self.screen, 
                LINE_COLOR, 
                (self.board_x + i * CELL_SIZE, self.board_y),
                (self.board_x + i * CELL_SIZE, self.board_y + BOARD_SIZE),
                5
            )
            
            pygame.draw.line(
                self.screen, 
                LINE_COLOR, 
                (self.board_x, self.board_y + i * CELL_SIZE),
                (self.board_x + BOARD_SIZE, self.board_y + i * CELL_SIZE),
                5
            )
    
    def draw_symbols(self):
        """Dessine les symboles X et O sur le plateau"""
        for row in range(3):
            for col in range(3):
                cell_value = self.game.board[row][col]
                if cell_value != ' ':
                    center_x = self.board_x + col * CELL_SIZE + CELL_SIZE // 2
                    center_y = self.board_y + row * CELL_SIZE + CELL_SIZE // 2
                    
                    if cell_value == 'X':
                        
                        color = X_COLOR
                        size = 50
                        
                        pygame.draw.line(
                            self.screen, color,
                            (center_x - size, center_y - size),
                            (center_x + size, center_y + size),
                            8
                        )
                        
                        pygame.draw.line(
                            self.screen, color,
                            (center_x + size, center_y - size),
                            (center_x - size, center_y + size),
                            8
                        )
                    else:  
                        
                        color = O_COLOR
                        radius = 40
                        pygame.draw.circle(
                            self.screen, color,
                            (center_x, center_y), radius, 8
                        )
    
    def draw_text(self):
        """Dessine le texte à l'écran"""
       
        title = self.title_font.render("🎮 TIC-TAC-TOE 🎮", True, TEXT_COLOR)
        title_rect = title.get_rect(center=(WIDTH//2, MARGIN))
        self.screen.blit(title, title_rect)
        
        
        if self.game.game_over:
            if self.game.winner:
                status_text = f"Le joueur {self.game.winner} a gagné!"
                color = X_COLOR if self.game.winner == 'X' else O_COLOR
            else:
                status_text = "Match nul!"
                color = (149, 165, 166)
        else:
            status_text = f"Tour du joueur: {self.game.current_player}"
            color = X_COLOR if self.game.current_player == 'X' else O_COLOR
        
        status = self.status_font.render(status_text, True, color)
        status_rect = status.get_rect(center=(WIDTH//2, MARGIN + 40))
        self.screen.blit(status, status_rect)
    
    def draw_button(self):
        """Dessine le bouton de réinitialisation"""
        mouse_pos = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER if self.reset_button.collidepoint(mouse_pos) else BUTTON_COLOR
        
        
        pygame.draw.rect(self.screen, button_color, self.reset_button, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), self.reset_button, 3, border_radius=10)
        
        
        button_text = self.button_font.render("Nouvelle Partie", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=self.reset_button.center)
        self.screen.blit(button_text, text_rect)
    
    def get_cell_from_pos(self, pos):
        """Convertit une position de souris en cellule du plateau"""
        x, y = pos
        
        
        if (self.board_x <= x <= self.board_x + BOARD_SIZE and
            self.board_y <= y <= self.board_y + BOARD_SIZE):
            
            col = (x - self.board_x) // CELL_SIZE
            row = (y - self.board_y) // CELL_SIZE
            return row, col
        
        return None, None
    
    def show_winner_message(self):
        """Affiche un message de fin de jeu"""
        if self.game.winner:
            message = f"Le joueur {self.game.winner} a gagné!"
        else:
            message = "Match nul!"
        
       
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  
        self.screen.blit(overlay, (0, 0))
        
        
        font = pygame.font.SysFont('arial', 48, bold=True)
        text = font.render(message, True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.screen.blit(text, text_rect)
        
        pygame.display.flip()
        pygame.time.wait(2000)  
    
    def reset_game(self):
        """Réinitialise le jeu"""
        self.game.reset_game()
    
    def run(self):
        """Boucle principale du jeu"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        
                        if self.reset_button.collidepoint(event.pos):
                            self.reset_game()
                        
                       
                        elif not self.game.game_over:
                            row, col = self.get_cell_from_pos(event.pos)
                            if row is not None and col is not None:
                                if self.game.make_move(row, col):
                                    if self.game.game_over:
                                        self.show_winner_message()
            
           
            self.screen.fill(BACKGROUND)
            self.draw_board()
            self.draw_symbols()
            self.draw_text()
            self.draw_button()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

def main():
    game = PygameTicTacToe()
    game.run()

if __name__ == "__main__":
    main()