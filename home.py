#from neighborhood import Neighborhood
import random

class Home:
  
  def create_home():
    numMonsters = random.randint(0, 10)
    if numMonsters != 0:
      print("[H]", end="")
    else:
      print("[ ]", end="")
