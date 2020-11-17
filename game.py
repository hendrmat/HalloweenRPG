import random
from player import Player
from neighborhood import Neighborhood

class Game:
  hood = Neighborhood()
  hood.create_grid()
  hero = Player(random.randint(100, 125), random.uniform(10, 20))
  hero.fill_inventory()
  hero.move_hero()

    
