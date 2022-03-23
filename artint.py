from player import Player




class Artint(Player):
  def __init__(self):
    self.gesture = ()
    super().__init__('artificial_intelligence')

  def artint_opponent(self):
    Player.gesture = ()