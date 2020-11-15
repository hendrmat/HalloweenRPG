import random
import array as arr
from weapon import *

class Player(object):
  
  def __init__(self, hp, atk):
    print("penis")
    self.hp = hp
    self.atk = atk
    self.inv_slot = []

  def fill_inventory(self, weapon):
    inv_slot = arr.array('i', [0])
    for i in range(1, 10):
      self.inv_slot.append(random.randint(1, 3))
      print(inv_slot)
  