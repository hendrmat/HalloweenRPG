from home import Home
import numpy

class Neighborhood():

  def create_grid(self):

    print("Oh no!  Those bad batches of candy turned everyone into monsters!")
    print("What a horrible night to have a curse...")
    print("\n")
    #dimension = int(input("Input the map size (min 4, max 10): "))
    rows = 5
    cols = 5
    grid = [[0 for i in range(5)] for j in range(5)] 
    #while dimension < 4 or dimension > 10:
      #dimension = int(input("Please enter a valid map size (min 4, max 10): "))
  
  
    for x in range(0, rows):
      print("\n")
      for y in range(0, cols):
        if (x == rows - 1 & y == cols - 1):
          grid[y][x] = "P"
        else:
          Home()
          grid[y][x] = "H"
          #print(grid[y][x])
        #house = Home()
        #monsters = Home.num_npcs
        #house.create_home(monsters)
        #grid[y][x] = house
        
        #if Home.monsters != 0:
          #print("H", end="")
        #else:
          #print("O", end="")
    print(numpy.matrix(grid))
  
