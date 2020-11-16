#from neighborhood import Neighborhood
from npc import NPC
import random

class Home(object):

  def __init__(self):
    self.monsters = []
    self.create_home()

  def create_home(self):
    
    person = NPC("Person", 100, -1)
    zombie = NPC("Zombie", random.randint(50, 100), random.randint(0, 10))
    vampire = NPC("Vampire", random.randint(100, 200), random.randint(10, 20))
    ghoul = NPC("Ghoul", random.randint(40, 80), random.randint(15, 30))
    werewolf = NPC("Werewolf", 200, random.randint(0, 40))

    npc_index = [person, zombie, vampire, ghoul, werewolf]
      
    num_npcs = random.randint(0, 10)
    for i in range(num_npcs):
      #print(num_npcs)
      self.monsters.append(npc_index[random.randint(1, 4)])
    print(self.monsters)  
