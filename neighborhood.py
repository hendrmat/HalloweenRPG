class Neighborhood:
  def grid():
    dimension = input("Please select the size of the neighborhood: ")
    while (dimension < 4):
      print("Invalid neighborhood size.  Please enter a size between 4 and 10")
    for i in range(dimension):
      print("\n")
    for j in range(dimension):
      print(" ")
