import random
import array as arr
from weapon import Weapon
from neighborhood import Neighborhood

class Player(object):
  
  def __init__(Neighborhood, max_hp, atk):
    Neighborhood.max_hp = max_hp
    Neighborhood.curr_hp = max_hp
    Neighborhood.atk = atk
    Neighborhood.inv_slot = []
    Neighborhood.uses = []
    

  def fill_inventory(Neighborhood):
    hershey = Weapon("Hershey Kisses", 1, 65535, 0, 1, 1, 1, 1)
    sour = Weapon("Sour Straws   ", random.uniform(1, 1.75), 2, 0, 2, 1, 1, 0)
    choco = Weapon("Chocolate Bars", random.uniform(2, 2.4), 4, 0, 1, 0, 1, 0)
    nerds = Weapon("Nerd Bombs    ", random.uniform(3.5, 5), 1, 0, 1, 1, 5, 1)

    default_weapon = [hershey.name]
    weapon_index = [sour.name, choco.name, nerds.name]
    init_uses_index = [sour.uses, choco.uses, nerds.uses]
    
    for i in range(0, 10):
      if i == 0:
        Neighborhood.inv_slot.append(default_weapon[0])
        Neighborhood.uses.append(65535)
      else:
        result = random.randint(0, 2)
        Neighborhood.inv_slot.append(weapon_index[result])
        Neighborhood.uses.append(init_uses_index[result])
    
    print("HP:", Neighborhood.curr_hp, "/", Neighborhood.max_hp)
    print("\n")
    print("Item Name      Remaining Uses")
    for j in range(0, 10):
      print(Neighborhood.inv_slot[j], Neighborhood.uses[j])
      
  def move_hero():
    for x in range(5):
      for y in range(5):
        if Neighborhood.grid[y][x] == "P":
          direction = input("Please enter a direction (n, s, e, w): ")
          while direction != "n" | direction != "s" | direction != "e" | direction != "w":
            direction = input("Invalid entry: Please enter a valid direction (n, s, e, w):")
          if direction == "n":
            if (y + 1) > 4:
              print("My parents say I can't go that far.  I should try another direction")
              move_hero()
            else:
              Neighborhood.grid[y][x] == "S"
              if Neighborhood.grid[y + 1][x] == "H":
                Neighborhood.grid[y + 1][x] == "P"
                fight_it_out()

          if direction == "s":
            if (y - 1) < 0:
              print("Never been there before, and I don't really wanna go")
              Game.move_hero()
            else:
              Neighborhood.grid[y][x] == "S"
              if Neighborhood.grid[y - 1][x] == "H":
                Neighborhood.grid[y - 1][x] == "P"
                Game.fight_it_out()

          if direction == "e":
            if (x + 1) > 4:
              print("I got grounded last time I went there.  I'll go another way")
              Game.move_hero()
            else:
              Neighborhood.grid[y][x] == "S"
              if Neighborhood.grid[y][x + 1] == "H":
                Neighborhood.grid[y][x + 1] == "P"
                Game.fight_it_out()

          if direction == "w":
            if (x - 1) < 0:
              print("Mom said not to approach those buildings with the red lights")
              Game.move_hero()
            else:
              Neighborhood.grid[y][x] == "S"
              if Neighborhood.grid[y][x - 1] == "H":
                Neighborhood.grid[y][x - 1] == "P"
                Game.fight_it_out()
  
  def fight_it_out():
    command = int(input("Some monsters draw near.  Command?: (select 0 - 9 on your inventory)"))
    while (command < 0 | command > 9) | uses[command] == 0:
      command = int(input("Invalid entry or out of uses, please enter 0 - 9 for your command"))
    uses[command] -= 1
    
                
