import random
import array as arr
from weapon import Weapon

class Player(object):
  
  def __init__(self, hp, atk):
    self.hp = hp
    self.atk = atk
    self.inv_slot = []

  def fill_inventory(self):
    #inv_slot = arr.array('i', [0])
    for i in range(0, 10):
      if i == 0:
        self.inv_slot.append(0)
      else:
        self.inv_slot.append(random.randint(1, 3))
      #print(self.inv_slot)
  