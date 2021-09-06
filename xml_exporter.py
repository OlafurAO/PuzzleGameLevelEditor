import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import xml.etree.ElementTree as ET

class XmlManager:
  def __init__(self) -> None:
    self.root = tk.Tk()
    self.root.withdraw()
    self.root.focus_force()

  def select_file(self):
    files = filedialog.askopenfilenames(parent=self.root)
    if len(files) == 0:
      return None

    if not files[0].endswith('.xml'):
      messagebox.showerror('Incorrect file format!', 'Please select a valid .xml file')
      return None

    return files[0]

  def save_file(self):
    file_name = filedialog.asksaveasfilename(parent=self.root, defaultextension='.xml') 

    if not file_name.endswith('.xml'):
      messagebox.showerror('Incorrect file format!', 'Please save as an .xml file')
      return None
    
    return file_name 

  def parse_xml_file(self, file):
    level_data = {}

    tree = ET.parse(file)
    tree_root = tree.getroot()

    size = tree_root.find('level_size')
    goal = tree_root.find('goal_pos')
    player = tree_root.find('player_pos')

    level_data['max_moves'] = int(tree_root.find('max_moves').text)
    level_data['level_size'] = self.get_xml_obj_pos(size)
    level_data['goal_pos'] = self.get_xml_obj_pos(goal)
    level_data['player_pos'] = self.get_xml_obj_pos(player)
    
    # TODO: more blocks
    blocks = {
      'block': tree_root.findall('obstacle_pos'),
      'fader_in': tree_root.findall('fader_in_pos'),
      'fader_out': tree_root.findall('fader_out_pos'),
      'fader_switch': tree_root.findall('fader_switch_pos'),
      'physics_block': tree_root.findall('physics_block_pos'),
      'lock': tree_root.findall('lock_pos'),
      'key': tree_root.findall('key_pos'),
      'flipper_r': tree_root.findall('flipper_r_pos'),
      'flipper_l': tree_root.findall('flipper_l_pos'),
      'flipper_u': tree_root.findall('flipper_u_pos'),
      'flipper_d': tree_root.findall('flipper_d_pos'),
      'flipper_switch': tree_root.findall('flipper_switch_pos')
    }

    level_data['blocks'] = {}
    for key in blocks:
      level_data['blocks'][key] = []
      for block in blocks[key]:
        if key == 'lock' or key == 'key':
          level_data['blocks'][key].append(
            self.get_xml_obj_pos_with_id(block)
          )
        else:  
          level_data['blocks'][key].append(
            self.get_xml_obj_pos(block)
          )
  
    return level_data
    
  @staticmethod
  def export_level_to_xml(file_name, level_cells, level_size, max_moves):
    goal_pos = None
    player_pos = None
    obstacle_pos = []
    fader_in_pos = []
    fader_out_pos = []
    physics_block_pos = []
    flipper_l_pos = []
    flipper_r_pos = []
    flipper_u_pos = []
    flipper_d_pos = []
    lock_pos = []
    lock_ids = []
    fader_switch = []
    flipper_switch = []
    key_pos = []
    key_ids = []

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
      elif cell_type == 'physics_block':
        physics_block_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_r':
        flipper_r_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_l':
        flipper_l_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_u':
        flipper_u_pos.append(cell.get_coordinates())    
      elif cell_type == 'flipper_d':
        flipper_d_pos.append(cell.get_coordinates())    
      elif cell_type == 'lock':
        lock_pos.append(cell.get_coordinates())    
        lock_ids.append(cell.get_id())
      elif cell_type == 'fader_switch':
        fader_switch.append(cell.get_coordinates())  
      elif cell_type == 'flipper_switch':
        flipper_switch.append(cell.get_coordinates())    
      elif cell_type == 'key':
        key_pos.append(cell.get_coordinates())
        key_ids.append(cell.get_id())


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

    for i in physics_block_pos:  
      xml_str += '\t<physics_block_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</physics_block_pos>\n'  

    for pos, id in zip(lock_pos, lock_ids):  
      xml_str += '\t<lock_pos>\n\t\t<id> ' + str(id) + ' </id>\n\t\t<x> ' + str(pos[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(pos[1]) + ' </y>\n\t</lock_pos>\n'    

    for pos, id in zip(key_pos, key_ids):    
      xml_str += '\t<key_pos>\n\t\t<id> ' + str(id) + ' </id>\n\t\t<x> ' + str(pos[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(pos[1]) + ' </y>\n\t</key_pos>\n'    

    for i in flipper_l_pos:  
      xml_str += '\t<flipper_l_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_l_pos>\n'    

    for i in flipper_r_pos:  
      xml_str += '\t<flipper_r_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_r_pos>\n'    

    for i in flipper_u_pos:  
      xml_str += '\t<flipper_u_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_u_pos>\n'    

    for i in flipper_d_pos:  
      xml_str += '\t<flipper_d_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_d_pos>\n'      

    for i in flipper_switch:  
      xml_str += '\t<flipper_switch_pos>\n\t\t<x> ' + str(i[0]) + ' </x>\n'
      xml_str += '\t\t<y> ' + str(i[1]) + ' </y>\n\t</flipper_switch_pos>\n'      


    # TODO: more blocks


    # player pos
    xml_str += '\t<player_pos>\n\t\t<x> ' + str(player_pos[0]) + ' </x>\n'
    xml_str += '\t\t<y> ' + str(player_pos[1]) + ' </y>\n\t</player_pos>\n'

    xml_str += '</level>'

    with open(file_name, 'w') as f:
      f.write(xml_str)

  def get_xml_obj_pos(self, obj):
    return (
      int(obj.find('x').text), 
      int(obj.find('y').text)
    )  

  def get_xml_obj_pos_with_id(self, obj):
    return (
      int(obj.find('x').text), 
      int(obj.find('y').text),
      int(obj.find('id').text),
    )
