import random
import array as arr
from weapon import Weapon
from neighborhood import Neighborhood

class Player(object):
  
  def __init__(self, max_hp, atk):
    self.max_hp = max_hp
    self.curr_hp = max_hp
    self.atk = atk
    self.inv_slot = []
    self.uses = []

  def fill_inventory(self):
    hershey = Weapon("Hershey Kisses", 1, 65535, 0, 1, 1, 1, 1)
    sour = Weapon("Sour Straws   ", random.uniform(1, 1.75), 2, 0, 2, 1, 1, 0)
    choco = Weapon("Chocolate Bars", random.uniform(2, 2.4), 4, 0, 1, 0, 1, 0)
    nerds = Weapon("Nerd Bombs    ", random.uniform(3.5, 5), 1, 0, 1, 1, 5, 1)

    default_weapon = [hershey.name]
    weapon_index = [sour.name, choco.name, nerds.name]
    init_uses_index = [sour.uses, choco.uses, nerds.uses]
    
    for i in range(0, 10):
      if i == 0:
        self.inv_slot.append(default_weapon[0])
        self.uses.append(65535)
      else:
        result = random.randint(0, 2)
        self.inv_slot.append(weapon_index[result])
        self.uses.append(init_uses_index[result])
    
    print("HP:", self.curr_hp, "/", self.max_hp)
    print("Attack Value:", self.atk)
    print("\n")
    print("Item Name      Remaining Uses")
    for j in range(0, 10):
      print(self.inv_slot[j], self.uses[j])
     
  def move_hero(self): 
    block = Neighborhood()   
    for x in range(5):
      for y in range(5):
        if block.grid[y][x] == "P":
          direction = input("Please enter a direction (n, s, e, w): ")
          while (direction != "n" and direction != "s" and direction != "e" and direction != "w"):
            direction = input("Invalid entry: Please enter a valid direction (n, s, e, w):")
          if direction == "n":
            if (y + 1) > 4:
              print("My parents say I can't go that far.  I should try another direction")
              self.move_hero()
            else:
              block.grid[y][x] == "S"
              if block.grid[y + 1][x] == "H":
                block.grid[y + 1][x] == "P"
                self.fight_it_out()

          if direction == "s":
            if (y - 1) < 0:
              print("Never been there before, and I don't really wanna go")
              self.move_hero()
            else:
              block.grid[y][x] == "S"
              if block.grid[y - 1][x] == "H":
                block.grid[y - 1][x] == "P"
                self.fight_it_out()

          if direction == "e":
            if (x + 1) > 4:
              print("I got grounded last time I went there.  I'll go another way")
              self.move_hero()
            else:
              block.grid[y][x] == "S"
              if block.grid[y][x + 1] == "H":
                block.grid[y][x + 1] == "P"
                self.fight_it_out()

          if direction == "w":
            if (x - 1) < 0:
              print("Mom said not to approach those buildings with the red lights")
              self.move_hero()
            else:
              block.grid[y][x] == "S"
              if block.grid[y][x - 1] == "H":
                block.grid[y][x - 1] == "P"
                self.fight_it_out()
  
  def fight_it_out(self):
    command = int(input("Some monsters draw near.  Command?: (select 0 - 9 on your inventory)"))
    while (command < 0 | command > 9) | uses[command] == 0:
      command = int(input("Invalid entry or out of uses, please enter 0 - 9 for your command"))
    uses[command] -= 1
    
                
