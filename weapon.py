import random

class Weapon:
  def __init__(self, name, attack, uses, invValue):
    self.name = name
    self.attack = attack
    self.uses = uses
    self.invValue = invValue

class HersheyKisses(Weapon):
  name = "Hershey Kisses"
  attack = 1
  uses = 65535
  invValue = 0

class SourStraws(Weapon):
  name = "Sour Straws"
  attack = random.uniform(1, 1.75)
  uses = 2
  invValue = 1

class ChocolateBars(Weapon):
  name = "Chocolate Bars"
  attack = random.uniform(2, 2.4)
  uses = 4
  invValue = 2

class NerdBombs(Weapon):
  name = "Nerd Bombs"
  attack = random.uniform(3.5, 5)
  uses = 1
  invValue = 3