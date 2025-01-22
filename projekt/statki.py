import sys
import pygame
import random

from button import Button
from settings import Settings
from ship import Ship

class Battleships:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.reset_game()

    def reset_game(self):
        """ Resetuje wszystkie zmienne do początkowego stanu """
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Statki")

        self.bg_color = self.settings.darkblue
        self.grid = [[0] * self.settings.grid_size for _ in range(self.settings.grid_size)]
        self.attempts = 0  
        self.ships = self.place_ships()
        
        total_grid_width = self.settings.grid_size * (self.settings.cell_size + self.settings.margin)
        total_grid_height = self.settings.grid_size * (self.settings.cell_size + self.settings.margin)
        self.offset_x = (self.settings.screen_width - total_grid_width) // 2
        self.offset_y = (self.settings.screen_height - total_grid_height) // 2 + 20
        self.game_over = False

    def place_ships(self):
        """ Losowo rozmieszcza statki na planszy, unikając kolizji i kontaktu """
        ship_sizes = [5, 4, 3, 3, 2]
        ships = []

        for size in ship_sizes:
            placed = False
            
            while not placed:
                x = random.randint(0, self.settings.grid_size - 1)
                y = random.randint(0, self.settings.grid_size - 1)
                direction = random.choice(["H", "V"])

                ship_cells = []
                for i in range(size):
                    if direction == "H":
                        ship_cells.append((x + i, y))
                    else:
                        ship_cells.append((x, y + i))

                if any(cx >= self.settings.grid_size or cy >= self.settings.grid_size for cx, cy in ship_cells):
                    continue

                if not self.check_collision(ship_cells):
                    ships.append(Ship(x, y, size, direction))

                    for cx, cy in ship_cells:
                        self.grid[cy][cx] = 1

                    placed = True 

        return ships

    def check_collision(self, ship_cells):
        """ Sprawdza, czy statek koliduje z innymi statkami lub ich najbliższym polem"""
        for cx, cy in ship_cells:
            if self.grid[cy][cx] == 1:  
                return True

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < self.settings.grid_size and 0 <= ny < self.settings.grid_size:
                        if self.grid[ny][nx] == 1:
                            return True
        return False

    def check_victory(self):
        """Sprawdza, czy wszystkie statki zostały zatopione"""
        return all(ship.is_sunk() for ship in self.ships)

    def show_start_screen(self):
        """Wyświetla ekran startowy"""
        font = pygame.font.Font(None, 72)
        start_text = font.render("Start Game", True, self.settings.white)
        instructions_text = pygame.font.Font(None, 36).render("Click to Start", True, self.settings.white)

        button_width = 300
        button_height = 80
        button_x = self.settings.screen_width // 2 - button_width // 2
        button_y = self.settings.screen_height // 2 - button_height // 2

        start_button = Button(
            self.screen,
            button_x, button_y,
            button_width, button_height,
            "Start Game", self.settings.green, self.settings.darkgreen, self.settings.white
        )

        waiting_for_click = True
        while waiting_for_click:
            self.screen.fill(self.bg_color)
            start_button.draw()
            self.screen.blit(instructions_text, (self.settings.screen_width // 2 - instructions_text.get_width() // 2, self.settings.screen_height // 2 + button_height // 2 + 10))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif start_button.is_clicked(event):
                    waiting_for_click = False

    def show_victory_screen(self):
        """Wyświetla ekran zwycięstwa z opcją Play Again"""
        font = pygame.font.Font(None, 72)
        font2 = pygame.font.Font(None, 50)
        victory_text = font.render("You Win!", True, self.settings.green)

        if self.attempts == 1:
            victory_text2 = font2.render(f"You missed {self.attempts} time", True, self.settings.darkgreen)
        else:
            victory_text2 = font2.render(f"You missed {self.attempts} times", True, self.settings.darkgreen)

        button_width = 300
        button_height = 80
        button_x = self.settings.screen_width // 2 - button_width // 2
        button_y = self.settings.screen_height // 2 + 100

        play_again_button = Button(
            self.screen,
            button_x, button_y,
            button_width, button_height,
            "Play Again", self.settings.green, self.settings.darkgreen, self.settings.white
        )

        self.screen.fill(self.bg_color)
        self.screen.blit(victory_text, (self.settings.screen_width // 2 - victory_text.get_width() // 2, self.settings.screen_height // 2 - victory_text.get_height() // 2))
        self.screen.blit(victory_text2, (self.settings.screen_width // 2 - victory_text2.get_width() // 2, self.settings.screen_height // 2 + victory_text2.get_height() + 10 // 2))

        play_again_button.draw()
        pygame.display.flip()

        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif play_again_button.is_clicked(event):
                    self.reset_game()
                    waiting_for_click = False

    def check_events(self):
        """Sprawdza kliknięcia"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.check_guess(x, y)
                
                  

    def check_guess(self, x, y):
        col = (x - self.offset_x) // (self.settings.cell_size + self.settings.margin)
        row = (y - self.offset_y) // (self.settings.cell_size + self.settings.margin)
        if 0 <= col < self.settings.grid_size and 0 <= row < self.settings.grid_size:
                    
            hit = False
            if self.grid[row][col] == 0:
                self.attempts += 1
            for ship in self.ships:
                if ship.check_hit(col, row):
                    hit = True
                    break
            
            self.grid[row][col] = 2 if hit else 3

    def draw_grid(self):
        """ Rysowanie planszy na środku ekranu """
        #Cyfry
        font = pygame.font.Font(None, 30)
        for row in range(self.settings.grid_size): #grid size to 10
            text = font.render(str(row + 1), True, self.settings.white)
            self.screen.blit(text, (self.offset_x - 30, self.offset_y + (self.settings.cell_size + self.settings.margin) * row + self.settings.cell_size // 2 - text.get_height() // 2))

        # Litery
        for col in range(self.settings.grid_size):
            letter = chr(65 + col)  # 65 to A
            text = font.render(letter, True, self.settings.white)
            self.screen.blit(text, (self.offset_x + (self.settings.cell_size + self.settings.margin) * col + self.settings.cell_size // 2 - text.get_width() // 2, self.offset_y - 30))

        # Okienka
        for row in range(self.settings.grid_size):
            for col in range(self.settings.grid_size):
                cell_value = self.grid[row][col]
                color = self.get_cell_color(cell_value)
                pygame.draw.rect(self.screen, color,
                                 [self.offset_x + (self.settings.cell_size + self.settings.margin) * col,
                                  self.offset_y + (self.settings.cell_size + self.settings.margin) * row,
                                  self.settings.cell_size, self.settings.cell_size])
                pygame.draw.rect(self.screen, self.settings.black,
                                 [self.offset_x + (self.settings.cell_size + self.settings.margin) * col,
                                  self.offset_y + (self.settings.cell_size + self.settings.margin) * row,
                                  self.settings.cell_size, self.settings.cell_size], 1)

    def get_cell_color(self, cell_value):
        """ Zwraca odpowiedni kolor dla danej komórki """
        if cell_value == 0:
            return self.settings.blue  # Woda
        elif cell_value == 1:
            return self.settings.gray  # Statek
        elif cell_value == 2:
            return self.settings.red  # Trafiony statek
        elif cell_value == 3:
            return self.settings.white  # Pudło

    def update_screen(self):
        """Wyświetla zmiany ekranu"""
        self.screen.fill(self.bg_color)
        self.draw_grid()
        self.show_attempts()
        pygame.display.flip()

    def show_attempts(self):
        """Wyświetla liczbę prób na ekranie"""
        font = pygame.font.Font(None, 36)
        text = font.render(f"Attempts: {self.attempts}", True, self.settings.white)
        self.screen.blit(text, (20, 20))

    def run_game(self):
        """Działanie gry"""
        self.show_start_screen()
        while not self.game_over:
            self.check_events()
            self.update_screen()
            if self.check_victory():
                pygame.time.delay(250)
                self.show_victory_screen()


if __name__ == '__main__':
    battleships = Battleships()
    battleships.run_game()
