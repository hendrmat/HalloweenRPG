import random
from player import Player
from neighborhood import Neighborhood

class Game:
  hood = Neighborhood()
  hood.create_grid()
  hero = Player(random.randint(100, 125), random.uniform(10, 20))
  hero.fill_inventory()

  def move_hero():
    for x in range(5):
      for y in range(5):
        if self.grid[y][x] == "P":
          direction = input("Please enter a direction (n, s, e, w): ")
          while direction != "n" | direction != "s" | direction != "e" | direction != "w":
            direction = input("Invalid entry: Please enter a valid direction (n, s, e, w):")
          #if (y + 1) > 4 | (x + 1) > 4 | (y - 1) < 0 | (x - 1) < 0:
            #print("My parents say I can't go that far.  I should try another direction")
          if direction == "n":
            if (y + 1) > 4:
              print("My parents say I can't go that far.  I should try another direction")
              Game.move_hero()
            else:
              self.grid[y][x] == "S"
              if self.grid[y + 1][x] == "H":
                self.grid[y + 1][x] == "P"
                Game.fight_it_out()

          if direction == "s":
            if (y - 1) < 0:
              print("Never been there before, and I don't really wanna go")
              Game.move_hero()
            else:
              self.grid[y][x] == "S"
              if self.grid[y - 1][x] == "H":
                self.grid[y - 1][x] == "P"
                Game.fight_it_out()

          if direction == "e":
            if (x + 1) > 4:
              print("I got grounded last time I went there.  I'll go another way")
              Game.move_hero()
            else:
              self.grid[y][x] == "S"
              if self.grid[y][x + 1] == "H":
                self.grid[y][x + 1] == "P"
                Game.fight_it_out()

          if direction == "w":
            if (x - 1) < 0:
              print("Mom said not to approach those buildings with the red lights")
              Game.move_hero()
            else:
              self.grid[y][x] == "S"
              if self.grid[y][x - 1] == "H":
                self.grid[y][x - 1] == "P"
                Game.fight_it_out()

  def fight_it_out():
    command = int(input("Some monsters draw near.  Command?: (select 0 - 9 on your inventory)"))
    while (command < 0 | command > 9) | hero.uses[command] == 0:
      command = int(input("Invalid entry or out of uses, please enter 0 - 9 for your command"))
    hero.uses[command] -= 1
    
