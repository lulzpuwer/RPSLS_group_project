from human import Human
from artint import Artint
from player import Player
import random


class Game():
  def __init__(self):
      self.human = Human()
      self.art_int = Artint()
      self.player_one = Human
      self.player_two = ()

  def run_game(self):
    self.display_welcome()
    self.display_rules()
    self.choose_game_mode()

  def display_welcome(self):
    print('++++ Welcome to Rock, Paper, Scissor, Lizard, Spock! ++++')
    print(' ')

  def display_rules(self):
    print('The rules of the game are: ')
    print('    Rock beats Scissor and Lizard! ')
    print('    Paper beats Rock and Spock! ')
    print('    Scissor beats Paper and Lizard! ')
    print('    Lizard beats Paper and Spock! ')
    print('    Spock beats Rock and Scissor')
    print(' ')

  def choose_game_mode(self):
    player_choice = input('Press 1 for: single player, Press 2 for: multi-player?:  ')
    if player_choice == "1":
      self.player_two = self.art_int.artint_opponent
      self.player_turn()
    elif player_choice == "2":
      self.player_two = self.human.human_two
      self.player_turn()
    else:
      print('You Choose Poorly! ')
  

  def player_turn(self):
    print('your choices are!: ')

    for option in self.human.gesture:
      print(option)
    self.player_gesture = self.human.gesture[int(input('Input number of gesture!: '))]
    self.opponent_turn()


  def opponent_turn(self):
    if self.player_two == self.art_int.artint_opponent:
      self.player_two_ai_gesture = self.art_int.gesture[random.randrange(0,5)]
      
    elif self.player_two == self.human.human_two:
      print('Player two turn!: ')
      for option in self.human.gesture:
        print(option)
      self.player_two_gesture = self.human.gesture[int(input('Input number of gesture!: '))]
    self.result()


  def result(self):
    pass

  def display_winner(self):
    pass




