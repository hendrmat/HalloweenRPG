import random
import array as arr
from weapon import Weapon

class Player(object):
  
  def __init__(self, max_hp, atk):
    self.max_hp = max_hp
    self.curr_hp = max_hp
    self.atk = atk
    self.inv_slot = []
    self.uses = []
    

  def fill_inventory(self):
    hershey = Weapon("Hershey Kisses", 1, 65535, 0, 1, 1, 1, 1)
    sour = Weapon("Sour Straws   ", random.uniform(1, 1.75), 2, 0, 2, 1, 1, 0)
    choco = Weapon("Chocolate Bars", random.uniform(2, 2.4), 4, 0, 1, 0, 1, 0)
    nerds = Weapon("Nerd Bombs    ", random.uniform(3.5, 5), 1, 0, 1, 1, 5, 1)

    default_weapon = [hershey.name]
    weapon_index = [sour.name, choco.name, nerds.name]
    init_uses_index = [sour.uses, choco.uses, nerds.uses]
    
    for i in range(0, 10):
      if i == 0:
        self.inv_slot.append(default_weapon[0])
        self.uses.append(65535)
      else:
        result = random.randint(0, 2)
        self.inv_slot.append(weapon_index[result])
        self.uses.append(init_uses_index[result])
    
    print("HP:", self.curr_hp, "/", self.max_hp)
    print("\n")
    print("Item Name      Remaining Uses")
    for j in range(0, 10):
      print(self.inv_slot[j], self.uses[j])

    