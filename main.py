import pygame
from level_canvas import LevelCanvas

pygame.init()

screen_size = (1400, 800)
game_display = pygame.display.set_mode(screen_size)


def draw(level):
  game_display.fill((0, 0, 0))
  level.draw_level(game_display)
  #pygame.display.flip()
  pygame.display.update();


def main():
  level_canvas = LevelCanvas()
  quit_editor = False

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

    draw(level_canvas)


if __name__ == '__main__':
  main()
