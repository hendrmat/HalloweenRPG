import random

class NPC(object):
  numNPCs = 0
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack

class Person(NPC):
  def __init__(self):
    super().__init__("Person", 100, -1)

class Zombie(NPC):
  def __init__(self):
    super().__init__("Zombie", random.randint(50, 100), 
    random.randint(0, 10))

class Vampire(NPC):
  def __init__(self):
    super().__init__("Vampire", random.randint(100-200), 
    random.randint(10-20))

class Ghoul(NPC):
  def __init__(self):
    super().__init__("Ghoul", random.randint(40, 80), 
    random.randint(15, 30))
    
class Werewolf(NPC):
  def __init__(self):
    super().__init__("Werewolf", 200, random.randint(0, 40))

   