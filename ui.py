import pygame

class UI:
  def __init__(self, screen_size, cell_type_display_info, xml_manager) -> None:
    pygame.font.init()
    self.init_text()
    self.screen_size = screen_size
    self.cell_type_display_info = cell_type_display_info
    self.xml_manager = xml_manager
    self.width = 250

  def draw_ui(self, game_display, selected_cell_type, max_moves):
    x = self.screen_size[0] - self.width
    pygame.draw.rect(
      game_display, (27, 24, 33), pygame.Rect(
        x - 20, 0, self.width + 20, self.screen_size[1]
      )
    )

    pygame.draw.rect(
      game_display, (111, 125, 140), pygame.Rect(
        self.buttons[6][0], self.buttons[6][1], 
        self.buttons[6][2], self.buttons[6][3]
      )
    )

    game_display.blit(self.load_text, (x - 100, 0))

    pygame.draw.rect(
      game_display, (111, 125, 140), pygame.Rect(
        self.buttons[7][0], self.buttons[7][1], 
        self.buttons[7][2], self.buttons[7][3]
      )
    )

    game_display.blit(self.save_text, (x - 100, 60))

    pygame.draw.rect(
      game_display, (111, 125, 140), pygame.Rect(
        self.buttons[8][0], self.buttons[8][1], 
        self.buttons[8][2], self.buttons[8][3]
      )
    )

    game_display.blit(self.reset_text, (x - 100, 120))

    pygame.draw.rect(
      game_display, (111, 125, 140), pygame.Rect(
        self.buttons[9][0], self.buttons[9][1], 
        self.buttons[9][2], self.buttons[9][3]
      )
    )

    game_display.blit(self.randomize_text, (x - 100, 180))

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
            self.cell_type_display_info[cell_type]['x_pos'] - 20,
            self.cell_type_display_info[cell_type]['y_pos'] + 7,
            10, 10
          )
        )
  
      pygame.draw.rect(
        game_display, self.cell_type_display_info[cell_type]['color'], pygame.Rect(
          self.cell_type_display_info[cell_type]['x_pos'],
          self.cell_type_display_info[cell_type]['y_pos'],    
          25, 25,
        ), 2 if cell_type == 'fader_out' else 0
      )

      game_display.blit(
        self.cell_type_texts[cell_type], 
        (self.cell_type_display_info[cell_type]['x_pos'] + 35, 
        self.cell_type_display_info[cell_type]['y_pos'] - 14)
      )

  def select_level_file(self):
    file = self.xml_manager.select_file()    
    return file

  def save_level_file(self):
    file_name = self.xml_manager.save_file()  
    return file_name
      
  def init_text(self):
    self.font = pygame.font.Font('fonts/pixeled.ttf', 16)
    self.load_text = self.font.render('Load', False, (255, 255, 255))
    self.save_text = self.font.render('Save', False, (255, 255, 255))
    self.reset_text = self.font.render('Reset', False, (255, 255, 255))
    self.randomize_text = self.font.render('Rand', False, (255, 255, 255))
    self.level_size_text = self.font.render('Level size', False, (255, 255, 255))
    self.x_text = self.font.render('X: ', False, (255, 255, 255))
    self.y_text = self.font.render('Y: ', False, (255, 255, 255))
    self.move_text = self.font.render('Moves: ', False, (255, 255, 255))

  def init_buttons(self):
    self.buttons = [
      # x, y, width, height
      (self.screen_size[0] - 20, 30, 40, 40),
      (self.screen_size[0] - 40, 32, 40, 40),
      (self.screen_size[0] - 20, 70, 40, 40),
      (self.screen_size[0] - 40, 72, 40, 40),

      (self.screen_size[0] - 20, 110, 40, 40),
      (self.screen_size[0] - 40, 112, 40, 40),
      (self.screen_size[0] - self.width - 120, 0, 100, 50),
      (self.screen_size[0] - self.width - 120, 60, 100, 50),
      (self.screen_size[0] - self.width - 120, 120, 100, 50),
      (self.screen_size[0] - self.width - 120, 180, 100, 50)
    ] 

    self.plus_icon = self.font.render('+', False, (255, 255, 255)) 
    self.minus_icon = self.font.render('-', False, (255, 255, 255)) 

  def check_for_button_click(self, mouse_pos):
    for i in range(len(self.buttons)):
      if self.buttons[i][0] <= mouse_pos[0] <= self.buttons[i][0] + self.buttons[i][2]:
        if self.buttons[i][1] <= mouse_pos[1] <= self.buttons[i][1] + self.buttons[i][3]:
          return i

    return ''    

  def set_level_size_text(self, size_x, size_y):
    self.x_val_text = self.font.render(str(size_x), False, (255, 255, 255))
    self.y_val_text = self.font.render(str(size_y), False, (255, 255, 255))

  def set_cell_type_texts(self):
    self.cell_type_texts = {
      'block': self.font.render('(1)  Block', False, (255, 255, 255)),
      'player': self.font.render('(2) Player', False, (255, 255, 255)),
      'goal': self.font.render('(3) Goal', False, (255, 255, 255)),
      'fader_in': self.font.render('(4) Fader-i', False, (255, 255, 255)),
      'fader_out': self.font.render('(5) Fader-o', False, (255, 255, 255)),
      'bouncer': self.font.render('(6) Bouncer', False, (255, 255, 255)),
      'lock': self.font.render('(7) Lock', False, (255, 255, 255)),
      'fader_switch': self.font.render('(8) Fa-switch', False, (255, 255, 255)),
      'flipper_switch': self.font.render('(9) Fl-switch', False, (255, 255, 255)),
      'flipper_l': self.font.render('(F1) Flipper-l', False, (255, 255, 255)),
      'flipper_r': self.font.render('(F2) Flipper-r', False, (255, 255, 255)),
      'flipper_u': self.font.render('(F3) Flipper-u', False, (255, 255, 255)),
      'flipper_d': self.font.render('(F4) Flipper-d', False, (255, 255, 255)),
    } 
