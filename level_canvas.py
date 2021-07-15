import pygame
from level_cell import LevelCell
from xml_exporter import XmlExporter


class LevelCanvas:
  def __init__(self, screen_size) -> None:
    self.xml_exporter = XmlExporter()
    self.screen_size = screen_size

    self.max_moves = 5
    self.cell_size = 80
    self.level_cells = []
    self.level_cell_locations = []

    self.scroll_x_direction = 0
    self.scroll_y_direction = 0
    self.x_scroll_offset = 0
    self.y_scroll_offset = 0
    self.scroll_speed = 0.5

    self.selected_cell_type = 'block'
    self.player_placed = False
    self.goal_placed = False

    self.highest_x_pos = 0
    self.highest_y_pos = 0

  def set_level_size(self, size_x, size_y):
     self.size_x = size_x
     self.size_y = size_y

  def draw_level(self, game_display):
    for cell, cell_pos in zip(self.level_cells, self.level_cell_locations):
      coordinates = cell_pos
      cell_type = cell.get_cell_type()
      color = self.get_cell_color(cell_type)

      pygame.draw.rect(
        game_display, color, pygame.Rect(
          coordinates[0],
          coordinates[1],
          self.cell_size,
          self.cell_size
        ), 1 if cell_type == 'empty' else 0
      )

  def export_xml(self):
    try:
      self.xml_exporter.export_xml(self.level_cells, (self.size_x, self.size_y), self.max_moves)
      print('success')
    except:
      print('error')

  def init_level_cells(self):
    existing_coordinates = self.get_existing_coordinates()
    
    for y in range(0, self.size_y, self.cell_size):
      for x in range(0, self.size_x, self.cell_size):
        if (x, y) not in existing_coordinates:
          self.level_cells.append(LevelCell(x, y, 'empty'))
          self.level_cell_locations.append((x + self.x_scroll_offset, y + self.y_scroll_offset))

        if x > self.highest_x_pos:
          self.highest_x_pos = x
      if y > self.highest_y_pos:
        self.highest_y_pos = y    

  def init_cell_type_display(self):
    cell_type_display = {
      'block': {
        'color': self.get_cell_color('block'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 200
      },
      'player': {
        'color': self.get_cell_color('player'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 230
      },
      'goal': {
        'color': self.get_cell_color('goal'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 260
      },
      'fader_in': {
        'color': self.get_cell_color('fader_in'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 290
      },
      'fader_out': {
        'color': self.get_cell_color('fader_out'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 320
      },
      'bouncer': {
        'color': self.get_cell_color('bouncer'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 350
      },
      'lock': {
        'color': self.get_cell_color('lock'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 380
      }, 
      'fader_switch': {
        'color': self.get_cell_color('fader_switch'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 410
      },
      'flipper_r': {
        'color': self.get_cell_color('flipper'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 440
      },
      'flipper_l': {
        'color': self.get_cell_color('flipper'),
        'x_pos': self.screen_size[0] - 190,
        'y_pos': 470
      },
    }

    return cell_type_display

  def shrink_level_x(self):
    tmp_list_cells = []
    tmp_list_locations = []

    for cell, location in zip(self.level_cells, self.level_cell_locations):
      if cell.get_coordinates()[0] != self.highest_x_pos:
        tmp_list_cells.append(cell)
        tmp_list_locations.append(location)

    self.level_cells = tmp_list_cells
    self.level_cell_locations = tmp_list_locations
    self.highest_x_pos -= 80

  def shrink_level_y(self):
    tmp_list_cells = []
    tmp_list_locations = []

    for cell, location in zip(self.level_cells, self.level_cell_locations):
      if cell.get_coordinates()[1] != self.highest_y_pos:
        tmp_list_cells.append(cell)
        tmp_list_locations.append(location)

    self.level_cells = tmp_list_cells
    self.level_cell_locations = tmp_list_locations
    self.highest_y_pos -= 80

  def handle_key_down(self, key):
    if key == pygame.K_1:
      self.selected_cell_type = 'block'
    if key == pygame.K_2:
      self.selected_cell_type = 'player'
    elif key == pygame.K_3:
      self.selected_cell_type = 'goal'
    elif key == pygame.K_4:
      self.selected_cell_type = 'fader_in'
    elif key == pygame.K_5:
      self.selected_cell_type = 'fader_out'  
    elif key == pygame.K_6:
      self.selected_cell_type = 'bouncer'
    elif key == pygame.K_7:
      self.selected_cell_type = 'lock'
    elif key == pygame.K_8:
      self.selected_cell_type = 'fader_switch'
    elif key == pygame.K_9:
      self.selected_cell_type = 'flipper_r' 
    elif key == pygame.K_0:
      self.selected_cell_type = 'flipper_l'   

    if key == pygame.K_LEFT or key == pygame.K_a:
      self.scroll_x_direction = 1
    elif key == pygame.K_RIGHT or key == pygame.K_d:
      self.scroll_x_direction = -1
    if key == pygame.K_UP or key == pygame.K_w:
      self.scroll_y_direction = 1
    elif key == pygame.K_DOWN or key == pygame.K_s:
      self.scroll_y_direction = -1 

    elif key == pygame.K_SPACE:
      self.export_xml()
    elif key == pygame.K_q:
      self.clear_canvas()    

  def handle_left_click(self, mouse_pos):
    index = self.get_clicked_cell_index(mouse_pos)
    if index != -1:
      if not (self.selected_cell_type == 'player' and self.player_placed)\
        and not (self.selected_cell_type == 'goal' and self.goal_placed):
        self.level_cells[index].set_cell_type(self.selected_cell_type)

        if self.selected_cell_type == 'player':
          self.player_placed = True
        elif self.selected_cell_type == 'goal':
          self.goal_placed = True

  def handle_right_click(self, mouse_pos):
    index = self.get_clicked_cell_index(mouse_pos)
    if index != -1:
      cell_type = self.level_cells[index].get_cell_type()
      if cell_type == 'player':
        self.player_placed = False
      elif cell_type == 'goal':
        self.goal_placed = False

      self.level_cells[index].set_cell_type('empty')

  def handle_canvas_scroll(self):
    if self.scroll_x_direction != 0:
      self.scroll_canvas_x(self.scroll_x_direction)

    if self.scroll_y_direction != 0:
      self.scroll_canvas_y(self.scroll_y_direction)  

  def reset_scroll_directions(self):
    self.scroll_x_direction = 0
    self.scroll_y_direction = 0

  def scroll_canvas_x(self, direction):
    for i in range(len(self.level_cell_locations)):
      new_x = self.level_cell_locations[i][0] + (direction * self.scroll_speed)
      curr_y = self.level_cell_locations[i][1]
      self.level_cell_locations[i] = (new_x, curr_y)      
    self.x_scroll_offset += (direction * self.scroll_speed)

  def scroll_canvas_y(self, direction):
    for i in range(len(self.level_cell_locations)):
      new_y = self.level_cell_locations[i][1] + (direction * self.scroll_speed)
      curr_x = self.level_cell_locations[i][0]
      self.level_cell_locations[i] = (curr_x, new_y)
    self.y_scroll_offset += (direction * self.scroll_speed)

  def modify_move_count(self, modifier):
    self.max_moves += modifier
    if self.max_moves < 0:
      self.max_moves = 0

  def clear_canvas(self,):
    self.level_cells = []
    self.init_level_cells()

  def get_clicked_cell_index(self, mouse_pos):
    for i in range(len(self.level_cell_locations)):
      cell_coordinates = self.level_cell_locations[i]
      if cell_coordinates[0] <= mouse_pos[0] <= cell_coordinates[0] + self.cell_size:
        if cell_coordinates[1] <= mouse_pos[1] <= cell_coordinates[1] + self.cell_size:
          return i

    return -1

  def get_existing_coordinates(self):
    coordinates = []  
    for cell in self.level_cells:
      coordinates.append(cell.get_coordinates())

    return coordinates  

  def get_cell_type_display_info(self):
    return self.cell_type_display  

  def get_selected_cell_type(self):
    return self.selected_cell_type

  def get_max_moves(self):
    return self.max_moves  

  @staticmethod
  def get_cell_color(cell_type):
    if cell_type == 'goal':
      return 115, 251, 211
    elif cell_type == 'player':
      return 226, 109, 92
    elif cell_type == 'fader_in':
      return 200, 214, 230
    elif cell_type == 'fader_out':
      return 200, 214, 230, 0.5  
    elif cell_type == 'bouncer':
      return 171, 41, 65
    elif 'flipper' in cell_type:
      return 7, 196, 230
    elif cell_type == 'lock':
      return 51, 62, 64
    elif cell_type == 'fader_switch':
      return 0, 0, 0      
    elif cell_type == 'block' or cell_type == 'empty':
      return 255, 255, 255

    return None
