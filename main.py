from xml_exporter import XmlManager
import pygame
from level_canvas import LevelCanvas
from ui import UI

pygame.init()

screen_size = (1400, 1000)
game_display = pygame.display.set_mode(screen_size)
level_size = [480, 480]

xml_manager = XmlManager()
level_canvas = LevelCanvas(screen_size, xml_manager)
level_canvas.set_level_size(level_size[0], level_size[1])
level_canvas.init_level_cells()

def check_for_ui_click(ui, level_canvas, mouse_pos):
  button_click = ui.check_for_button_click(mouse_pos)

  if button_click != '':
    global level_size 
    if button_click == 0:
      level_size[0] += 80

    elif button_click == 1:
      if level_size[0] != 0:
        level_size[0] -= 80

    elif button_click == 2:
      level_size[1] += 80

    elif button_click == 3:
      if level_size[1] != 0:
        level_size[1] -= 80

    elif button_click == 4:
      level_canvas.modify_move_count(1)

    elif button_click == 5:
      level_canvas.modify_move_count(-1)

    elif button_click == 6:
      file = ui.select_level_file()
      if file != None:        
        level_canvas.load_level_from_file(file)        
        level_size = level_canvas.get_level_size()

    elif button_click == 7:
      file_name = ui.save_level_file()
      if file_name != None:
        level_canvas.export_xml(file_name)

    elif button_click == 8:
      level_canvas = LevelCanvas(screen_size, xml_manager)
      level_canvas.set_level_size(level_size[0], level_size[1])
      level_canvas.init_level_cells()    
      
    elif button_click == 9:
      level_canvas.load_random_level()

    level_canvas.set_level_size(level_size[0], level_size[1])
    ui.set_level_size_text(level_size[0], level_size[1])

    if button_click == 0 or button_click == 2:
      level_canvas.init_level_cells()
    elif button_click == 1:
      level_canvas.shrink_level_x()
    elif button_click == 3:
      level_canvas.shrink_level_y()  
        

def draw(level_canvas, ui):
  game_display.fill((0, 0, 0))
  level_canvas.draw_level(game_display)

  selected_cell_type = level_canvas.get_selected_cell_type()
  ui.draw_ui(game_display, selected_cell_type, level_canvas.get_max_moves())
  pygame.display.update()


def main():
  ui = UI(screen_size, level_canvas.init_cell_type_display(), xml_manager)
  ui.set_level_size_text(level_size[0], level_size[1])
  ui.set_cell_type_texts()
  ui.init_buttons()

  quit_editor = False

  while not quit_editor:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_editor = True

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          level_canvas.handle_left_click(pygame.mouse.get_pos())
          check_for_ui_click(ui, level_canvas, pygame.mouse.get_pos())

        elif event.button == 3:
          level_canvas.handle_right_click(pygame.mouse.get_pos())
          
      if event.type == pygame.KEYDOWN:
        level_canvas.handle_key_down(event.key)
      elif event.type == pygame.KEYUP:
        level_canvas.reset_scroll_directions()    
   
    level_canvas.handle_canvas_scroll()  

    draw(level_canvas, ui)


if __name__ == '__main__':
  main()
