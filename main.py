import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("Formula 1 header template (35) (1).avif", SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
class Sprite((pygame.sprite.Sprite)):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface(width, height)
        self.image.fill(
pygame.color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, height, width))
        self.image = self.image.get.rect()

def move(self, x_change):
    self.get.x = max(
min(self.get.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
     self.get.y = max(
min(self.get.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
    
screen = pygame.display.set_mode()

clock = pygame.time.Clock()
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                    and event.key == pygame.k.x):
         running = False

if not won:
   keys = pygame.get_pressed()
   x_change = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT])*MOVEMENT_SPEED
   y_change = (keys[pygame.K_DOWN]- keys[pygame.K_UP])*MOVEMENT_SPEED
   sprite1.move(x_change, y_change)

   if sprite1.rect.collliderect(sprite2.rect):
      all.sprites.remove(Sprite2)
      won = True