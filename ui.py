import pygame
import os

class UI:
  def __init__(self, screen_size) -> None:
    pygame.font.init()
    self.init_text()
    self.screen_size = screen_size
    self.width = 200

  def draw_ui(self, game_display):
    x = self.screen_size[0] - self.width
    pygame.draw.rect(
      game_display, (27, 24, 33), pygame.Rect(
        x, 0, self.width, self.screen_size[1]
      )
    )

    game_display.blit(self.screenSizeText, (x + 30, 0))
    game_display.blit(self.xText, (x + 10, 30))
    game_display.blit(self.yText, (x + 10, 70))

  def init_text(self):
    self.font = pygame.font.Font('fonts/pixeled.ttf', 16)

    self.screenSizeText = self.font.render('Level size', False, (255, 255, 255))
    self.xText = self.font.render('X: ', False, (255, 255, 255))
    self.yText = self.font.render('Y: ', False, (255, 255, 255))
