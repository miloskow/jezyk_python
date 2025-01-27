import pygame

class Button:
    def __init__(self, screen, x, y, width, height, text, color, hover_color, text_color):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """Rysuje przycisk, zmienia kolor po najechaniu myszką."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_color = (self.hover_color if self.rect.collidepoint(mouse_x, mouse_y) 
                        else self.color)
        
        pygame.draw.rect(self.screen, button_color, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2) 

        text_surface = self.font.render(self.text, True, self.text_color)
        text_x = (self.rect.x + (self.rect.width - text_surface.get_width()) // 2)
        text_y = (self.rect.y + (self.rect.height - text_surface.get_height()) // 2)
        self.screen.blit(text_surface, (text_x, text_y))

    def is_clicked(self, event):
        """Sprawdza, czy przycisk został kliknięty."""
        return (event.type == pygame.MOUSEBUTTONDOWN and 
                self.rect.collidepoint(event.pos))
