import random

class Weapon(object):
  def __init__(self, name, attack, uses):
    self.name = name
    self.attack = attack
    self.uses = uses

class HersheyKisses(Weapon):
  def __init__(self):
    super().__init__("Hershey Kisses", 1, 65535)

class SourStraws(Weapon):
  def __init__(self):
    super().__init__("Sour Straws", random.uniform(1, 1.75), 2)

class ChocolateBars(Weapon):
  def __init__(self):
    super().__init__("Chocolate Bars", random.uniform(2, 2.4), 4)
  
class NerdBombs(Weapon):
  def __init__(self):
    super().__init__("Nerd Bombs", random.uniform(3.5, 5), 1)
  