import random
import array as arr
from weapon import Weapon

class Player(object):
  def __init__(self):
    self.hp = random.randint(100, 125)
    self.atk = random.uniform(10, 20)
    self.invSlot = arr.array('i', [0])
    print(self.invSlot[0])
    #for i in range(1, 10):
      #invSlot.append(random.randint(1, 3))
    #print(Weapon.invValue(invSlot))