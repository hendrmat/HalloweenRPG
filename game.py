import random
from player import Player
from neighborhood import Neighborhood

class Game:
  hood = Neighborhood()
  hood.create_grid()
  hero = Player(random.randint(100, 125), random.uniform(10, 20))
  hero.fill_inventory()
  hero.move_hero()

  def fight_it_out():
    command = int(input("Some monsters draw near.  Command?: (select 0 - 9 on your inventory)"))
    while (command < 0 | command > 9) | hero.uses[command] == 0:
      command = int(input("Invalid entry or out of uses, please enter 0 - 9 for your command"))
    hero.uses[command] -= 1
    
