import tkinter

class XmlExporter:
  @staticmethod
  def export_xml(level_cells, level_size, max_moves):
    goal_pos = None
    player_pos = None
    obstacle_pos = []
    fader_in_pos = []
    fader_out_pos = []
    bouncer_pos = []
    flipper_r_pos = []
    flipper_l_pos = []
    lock_pos = []
    fader_switch = []


    for cell in level_cells:
      cell_type = cell.get_cell_type()
      if cell_type == 'goal':
        goal_pos = cell.get_coordinates()
      elif cell_type == 'player':
        player_pos = cell.get_coordinates()
      elif cell_type == 'block':
        obstacle_pos.append(cell.get_coordinates())
      elif cell_type == 'fader_in':
        fader_in_pos.append(cell.get_coordinates())  
      elif cell_type == 'fader_out':
        fader_out_pos.append(cell.get_coordinates())    
      elif cell_type == 'bouncer':
        bouncer_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_r':
        flipper_r_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_l':
        flipper_l_pos.append(cell.get_coordinates())    
      elif cell_type == 'lock':
        lock_pos.append(cell.get_coordinates())    
      elif cell_type == 'fader_switch':
        fader_switch.append(cell.get_coordinates())  

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
      xml_str += '\t<obstacle_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</obstacle_pos>\n'

    # fader in pos
    for i in fader_in_pos:
      xml_str += '\t<fader_in_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</fader_in_pos>\n'  

    # fader out pos
    for i in fader_out_pos:
      xml_str += '\t<fader_out_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</fader_out_pos>\n'    

    for i in fader_switch:  
      xml_str += '\t<fader_switch_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</fader_switch_pos>\n'    

    for i in bouncer_pos:  
      xml_str += '\t<bouncer_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</bouncer_pos>\n'  

    for i in lock_pos:  
      xml_str += '\t<lock_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</lock_pos>\n'      

    for i in flipper_r_pos:  
      xml_str += '\t<flipper_r_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_r_pos>\n'      

    for i in flipper_l_pos:  
      xml_str += '\t<flipper_l_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_l_pos>\n'    

    # player pos
    xml_str += '\t<player_pos>\n\t\t<x> ' + str(player_pos[0]) + ' </x>\n'
    xml_str += '\t\t<y> ' + str(player_pos[1]) + ' </y>\n\t</player_pos>\n'

    xml_str += '\n</level>'

    with open('level.xml', 'w') as f:
      f.write(xml_str)





