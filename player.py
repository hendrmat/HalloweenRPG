import random
import array as arr
from weapon import Weapon

class Player:
  def __init__(self, hp, atk, invslot):
    hp = random.randint(100, 125)
    atk = random.uniform(10, 20)
    invSlot = arr.array('i', [0])
    print(invSlot[0])
    for i in range(1, 10):
      invSlot.append(random.randint(1, 3))
    print(Weapon.invValue(invSlot))