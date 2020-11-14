#from neighborhood import Neighborhood
import random
class Home:
  
  def createHome():
    numMonsters = random.randint(0, 10)
    if numMonsters != 0:
      print("[H]", end="")
    else:
      print("[ ]", end="")
