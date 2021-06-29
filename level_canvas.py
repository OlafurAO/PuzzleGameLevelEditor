import pygame
from level_cell import LevelCell
from xml_exporter import XmlExporter


class LevelCanvas:
  def __init__(self, screen_size) -> None:
    self.xml_exporter = XmlExporter()
    self.screen_size = screen_size

    self.size_x, self.size_y = 480, 480
    self.max_moves = 5
    self.cell_size = 80
    self.level_cells = []
    self.level_cell_locations = []

    self.scroll_x_direction = 0
    self.scroll_y_direction = 0
    self.scroll_speed = 0.5

    self.selected_cell_type = 'block'
    self.player_placed = False
    self.goal_placed = False

    self.init_level_cells()

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
    except:
      print('error')

  def init_level_cells(self):
    for y in range(0, self.size_y, self.cell_size):
      for x in range(0, self.size_x, self.cell_size):
        self.level_cells.append(LevelCell(x, y, 'empty'))
        self.level_cell_locations.append((x, y))

  def handle_key_down(self, key):
    if key == pygame.K_p:
      self.selected_cell_type = 'player'
    elif key == pygame.K_g:
      self.selected_cell_type = 'goal'
    elif key == pygame.K_b:
      self.selected_cell_type = 'block'

    elif key == pygame.K_LEFT:
      self.scroll_x_direction = 1
    elif key == pygame.K_RIGHT:
      self.scroll_x_direction = -1
    elif key == pygame.K_UP:
      self.scroll_y_direction = 1
    elif key == pygame.K_DOWN:
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

  def scroll_canvas_y(self, direction):
    for i in range(len(self.level_cell_locations)):
      new_y = self.level_cell_locations[i][1] + (direction * self.scroll_speed)
      curr_x = self.level_cell_locations[i][0]
      self.level_cell_locations[i] = (curr_x, new_y)

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

  @staticmethod
  def get_cell_color(cell_type):
    if cell_type == 'goal':
      return 115, 251, 211
    elif cell_type == 'player':
      return 226, 109, 92
    elif cell_type == 'block' or cell_type == 'empty':
      return 255, 255, 255

    return None


