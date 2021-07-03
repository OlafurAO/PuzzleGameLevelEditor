import pygame
import os

class UI:
  def __init__(self, screen_size, cell_type_display_info) -> None:
    pygame.font.init()
    self.init_text()
    self.screen_size = screen_size
    self.cell_type_display_info = cell_type_display_info
    self.width = 200

  def draw_ui(self, game_display, selected_cell_type, max_moves):
    x = self.screen_size[0] - self.width
    pygame.draw.rect(
      game_display, (27, 24, 33), pygame.Rect(
        x, 0, self.width, self.screen_size[1]
      )
    )

    game_display.blit(self.level_size_text, (x + 30, 0))

    game_display.blit(self.x_text, (x + 10, 30))
    game_display.blit(self.x_val_text, (x + 50, 30))
    game_display.blit(self.plus_icon, (self.buttons[0][0], self.buttons[0][1]))
    game_display.blit(self.minus_icon, (self.buttons[1][0], self.buttons[1][1]))

    game_display.blit(self.y_text, (x + 10, 70))
    game_display.blit(self.y_val_text, (x + 50, 70))
    game_display.blit(self.plus_icon, (self.buttons[2][0], self.buttons[2][1]))
    game_display.blit(self.minus_icon, (self.buttons[3][0], self.buttons[3][1]))

    game_display.blit(self.move_text, (x + 10, 110))
    game_display.blit(self.font.render(str(max_moves), False, (255, 255, 255)), (x + 120, 110))
    game_display.blit(self.plus_icon, (self.buttons[4][0], self.buttons[4][1]))
    game_display.blit(self.minus_icon, (self.buttons[5][0], self.buttons[5][1]))

    for cell_type in self.cell_type_display_info:
      if cell_type == selected_cell_type:
        pygame.draw.rect(
          game_display, (255, 255, 255), pygame.Rect(
            self.cell_type_display_info[cell_type]['x_pos'] - 30,
            self.cell_type_display_info[cell_type]['y_pos'] + 7,
            10, 10
          )
        )
  
      pygame.draw.rect(
        game_display, self.cell_type_display_info[cell_type]['color'], pygame.Rect(
          self.cell_type_display_info[cell_type]['x_pos'],
          self.cell_type_display_info[cell_type]['y_pos'],    
          25, 25
        ) 
      )

      game_display.blit(
        self.cell_type_texts[cell_type], 
        (self.cell_type_display_info[cell_type]['x_pos'] + 35, 
        self.cell_type_display_info[cell_type]['y_pos'] - 14)
      )
      
  def init_text(self):
    self.font = pygame.font.Font('fonts/pixeled.ttf', 16)

    self.level_size_text = self.font.render('Level size', False, (255, 255, 255))
    self.x_text = self.font.render('X: ', False, (255, 255, 255))
    self.y_text = self.font.render('Y: ', False, (255, 255, 255))
    self.move_text = self.font.render('Moves: ', False, (255, 255, 255))

  def init_buttons(self):
    self.buttons = [
      (self.screen_size[0] - 20, 30),
      (self.screen_size[0] - 40, 32),
      (self.screen_size[0] - 20, 70),
      (self.screen_size[0] - 40, 72),

      (self.screen_size[0] - 20, 110),
      (self.screen_size[0] - 40, 112),
    ] 

    self.plus_icon = self.font.render('+', False, (255, 255, 255)) 
    self.minus_icon = self.font.render('-', False, (255, 255, 255)) 

  def check_for_button_click(self, mouse_pos):
    for i in range(len(self.buttons)):
      if self.buttons[i][0] <= mouse_pos[0] <= self.buttons[i][0] + 40:
        if self.buttons[i][1] <= mouse_pos[1] <= self.buttons[i][1] + 40:
          return i

    return ''    

  def set_level_size_text(self, size_x, size_y):
    self.x_val_text = self.font.render(str(size_x), False, (255, 255, 255))
    self.y_val_text = self.font.render(str(size_y), False, (255, 255, 255))

  def set_cell_type_texts(self):
    self.cell_type_texts = {
      'block': self.font.render('(B)lock', False, (255, 255, 255)),
      'player': self.font.render('(P)layer', False, (255, 255, 255)),
      'goal': self.font.render('(G)oal', False, (255, 255, 255))
    } 
