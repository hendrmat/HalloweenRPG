import random
import array as arr
from weapon import Weapon

class Player(object):
  
  def __init__(self, hp, atk):
    self.hp = hp
    self.atk = atk
    self.inv_slot = []

  def fill_inventory(self):
    hershey = Weapon("Hershey Kisses", 1, 65535)
    sour = Weapon("Sour Straws", random.uniform(1, 1.75), 2)
    choco = Weapon("Chocolate Bars", random.uniform(2, 2.4), 4)
    nerds = Weapon("Nerd Bombs", random.uniform(3.5, 5), 1)

    weapon_index = [[sour.name, sour.uses], [choco.name, choco.uses], [nerds.name, nerds.uses]]
    
    for i in range(0, 10):
      if i == 0:
        self.inv_slot.append([hershey.name, hershey.uses])
      else:
        self.inv_slot.append(weapon_index[random.randint(0, 2)])

  