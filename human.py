from player import Player


class Human(Player):
  def __init__(self):
    self.gesture = ()
    super().__init__('Bob')

  def human_one(self, opponent):
    pass

  def human_two(self, opponent):
    pass
