import pygame
from level_canvas import LevelCanvas
from ui import UI

pygame.init()

screen_size = (1400, 800)
game_display = pygame.display.set_mode(screen_size)


def draw(level_canvas, ui):
  game_display.fill((0, 0, 0))
  level_canvas.draw_level(game_display)
  ui.draw_ui(game_display)
  pygame.display.update()


def main():
  level_canvas = LevelCanvas(screen_size)
  ui = UI(screen_size)

  quit_editor = False
  key_down = False

  while not quit_editor:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_editor = True

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          level_canvas.handle_left_click(pygame.mouse.get_pos())
        elif event.button == 3:
          level_canvas.handle_right_click(pygame.mouse.get_pos())
          
      if event.type == pygame.KEYDOWN:
        level_canvas.handle_key_down(event.key)
        key_down = True
      elif event.type == pygame.KEYUP:
        level_canvas.reset_scroll_directions()
        key_down = False
    
    if key_down:
      level_canvas.handle_canvas_scroll()  

    draw(level_canvas, ui)


if __name__ == '__main__':
  main()
