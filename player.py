import random
import array as arr
from weapon import Weapon

class Player(object):
  
  def __init__(self, hp, atk):
    self.hp = hp
    self.curr_hp = hp
    self.atk = atk
    self.inv_slot = []
    self.uses = []
    

  def fill_inventory(self):
    hershey = Weapon("Hershey Kisses", 1, 65535)
    sour = Weapon("Sour Straws   ", random.uniform(1, 1.75), 2)
    choco = Weapon("Chocolate Bars", random.uniform(2, 2.4), 4)
    nerds = Weapon("Nerd Bombs    ", random.uniform(3.5, 5), 1)

    weapon_index = [[sour.name], [choco.name], [nerds.name]]
    init_uses_index = [2, 4, 1]
    
    for i in range(0, 10):
      if i == 0:
        self.inv_slot.append([hershey.name])
        self.uses.append([65535])
      else:
        self.inv_slot.append(weapon_index[random.randint(0, 2)])
        if weapon_index[0]:
          self.uses.append([init_uses_index[0]])
        if weapon_index[1]:
          self.uses.append([init_uses_index[1]])
        if weapon_index[2]:
          self.uses.append([init_uses_index[2]])
    
    
    print("HP:", self.curr_hp, "/", self.hp)
    print("\n")
    print("Item Name          Remaining Uses")
    for j in range(0, 10):
      print(self.inv_slot[j], self.uses[j])

    