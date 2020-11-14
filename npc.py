import random

class NPC:
  def __init__(self, name, health, attack, npcValue):
    self.name = name
    self.health = health
    self.attack = attack
    self.npcValue = npcValue

  def Person(NPC):
    name = "Person"
    health = 100
    attack = -1
    npcValue = 0

  def Zombie(NPC):
    name = "Zombie"
    health = random.randint(50, 100)
    attack = random.randint(0, 10)
    npcValue = 1

  def Vampire(NPC):
    name = "Vampire"
    health = random.randint(100-200)
    attack = random.randint(10-20)
    npcValue = 2

  def Ghoul(NPC):
    name = "Ghoul"
    health = random.randint(40, 80)
    attack = random.randint(15, 30)
    npcValue = 3
  
  def Werewolf(NPC):
    name = "Werewolf"
    health = 200
    attack = random.randint(0, 40)
    npcValue = 4