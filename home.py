
from npc import NPC
import random

class Home:
  
  person = NPC("Person", 100, -1)
  zombie = NPC("Zombie", random.randint(50, 100), random.randint(0, 10))
  vampire = NPC("Vampire", random.randint(100, 200), random.randint(10, 20))
  ghoul = NPC("Ghoul", random.randint(40, 80), random.randint(15, 30))
  werewolf = NPC("Werewolf", 200, random.randint(0, 40))
  
  def create_home():
    monsters = random.randint(0, 10)
    if monsters != 0:
      print("[H]", end="")
    else:
      print("[S]", end="")
    #for i in range(0, monsters + 1):
