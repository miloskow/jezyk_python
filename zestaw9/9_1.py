import pygame
import random
import time

pygame.init()


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 400
SNOWFLAKE_SIZE = 20 


MAX_SNOWFLAKES = 10 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Płatki Śniegu")

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SNOWFLAKE_SIZE)
        self.y = 0
        self.speed = random.uniform(0.3, 1)
        self.rect = pygame.Rect(self.x, self.y, SNOWFLAKE_SIZE, SNOWFLAKE_SIZE)

    def fall(self):
        self.y += self.speed
        self.rect.y = self.y

    def reset(self):
        self.x = random.randint(0, WIDTH - SNOWFLAKE_SIZE)
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, SNOWFLAKE_SIZE, SNOWFLAKE_SIZE)

def draw_snowflakes(snowflakes):
    for snowflake in snowflakes:
        pygame.draw.rect(screen, WHITE, snowflake.rect)

def draw_score(score):
    font = pygame.font.SysFont("arial", 20)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def game():
    clock = pygame.time.Clock()
    snowflakes = [Snowflake() for _ in range(MAX_SNOWFLAKES)]
    score = 0
    game_over = False

    while not game_over:
        screen.fill(BLACK)  
        draw_score(score)  
        draw_snowflakes(snowflakes)  

     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for snowflake in snowflakes:
                    if snowflake.rect.collidepoint(mouse_x, mouse_y):
                        snowflake.reset()  
                        score += 1  

      
        for snowflake in snowflakes:
            snowflake.fall()

          
            if snowflake.rect.y > HEIGHT:
                game_over = True
                break

        
        pygame.display.flip()

        
        clock.tick(60)

    font = pygame.font.SysFont("arial", 40)
    end_text = font.render("Game Over!", True, WHITE)
    screen.blit(end_text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)  
    pygame.quit()

game()
