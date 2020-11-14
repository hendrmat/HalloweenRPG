from home import Home

class Neighborhood:
  print("Oh no!  Those bad batches of candy turned everyone into monsters!")
  print("What a horrible night to have a curse...")
  print("\n")
  dimension = int(input("Input the map size (min 4, max 10): "))
  while dimension < 4 or dimension > 10:
    input("Please enter a valid map size (min 4, max 10): ")
  for x in range(0, dimension):
    print("\n")
    for y in range(0, dimension):
      Home.createHome()
      print(" ", end="")
  
