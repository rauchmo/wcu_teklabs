import time

while True:
  x = input("Enter a projekt_number: ")
  print("Searching... Please wait")
  time.sleep(3)
  if x == "6969420":
      print("Projekt Martin Man Control Device found")
      y = input("Download Plans (y/n):")
      if (y == "y"):
        z = 0
        while (z != 100): 
          print("Downloading Plans "+z+"%")
          z = z + 1
          print("Download DONE")
      else:
        print("Abort")  
