#from neighborhood import Neighborhood
import random

class Home:
  
  def create_home():
    monsters = random.randint(0, 10)
    if monsters != 0:
      print("[H]", end="")
    else:
      print("[ ]", end="")
    #for i in range(0, monsters)