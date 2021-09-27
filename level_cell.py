# empty
# block
# player
# goal


class LevelCell:
  def __init__(self, x, y, cell_type):
    self.x = x
    self.y = y
    self.cell_type = cell_type

  def set_cell_type(self, new_type):
    self.cell_type = new_type

  def set_id(self, id):
    self.lock_id = id

  def get_coordinates(self):
    return self.x, self.y

  def get_cell_type(self):
    return self.cell_type

  def get_id(self):
    return self.lock_id
