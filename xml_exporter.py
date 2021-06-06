import tkinter

class XmlExporter:
  @staticmethod
  def export_xml(level_cells, level_size, max_moves):
    goal_pos = None
    player_pos = None
    obstacle_pos = []

    for cell in level_cells:
      cell_type = cell.get_cell_type()
      if cell_type == 'goal':
        goal_pos = cell.get_coordinates()
      elif cell_type == 'player':
        player_pos = cell.get_coordinates()
      elif cell_type == 'block':
        obstacle_pos.append(cell.get_coordinates())

    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n<level>\n'
    xml_str += '\t<max_moves>' + str(max_moves) + '</max_moves>\n'

    # level size
    xml_str += '\t<level_size>\n\t\t<x> ' + str(level_size[0]) + ' </x>\n'
    xml_str += '\t\t<y> ' + str(level_size[1]) + ' </y>\n\t</level_size>\n'

    # goal pos
    xml_str += '\t<goal_pos>\n\t\t<x> ' + str(goal_pos[0]) + ' </x>\n'
    xml_str += '\t\t<y> ' + str(goal_pos[1]) + ' </y>\n\t</goal_pos>\n'

    # obstacle pos
    for i in obstacle_pos:
      print(i)
      xml_str += '\t<obstacle_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</obstacle_pos>\n'

    # player pos
    xml_str += '\t<player_pos>\n\t\t<x> ' + str(player_pos[0]) + ' </x>\n'
    xml_str += '\t\t<y> ' + str(player_pos[1]) + ' </y>\n\t</player_pos>\n'

    xml_str += '\n</level>'

    with open('level.xml', 'w') as f:
      f.write(xml_str)





