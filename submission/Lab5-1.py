from sense_hat import SenseHat
# import random module
import random

# this function will take number of faces as an argument and returns random value within those faces
def rollAdice(f):
    return (random.randint(1, f))

# Calling function. This will return number between 1 to 8(passed as a parameter)
print(rollAdice(8))

s = SenseHat()

# Variable faces will take value from user
while True:

  try:
    faces = int(input("Enter number of faces of dice."))
    # Until user enter value between 1 to 64 it will ask user to enter number
    while (int(faces) > 65 or int(faces) <= 0):
        faces = int(input("Enter number which is less than 65 or less than 0."))
    break
  except:
    print("Invalid number")


# Outer loop will run for each row
outer = int(faces) / 8
# Outer loop an inner loop counter variables set as 0
i = 0
j = 0

# if faces are less the 8 then we are using faces variable value for inner loop  else we will use 8.
if(int(faces)<=8):
  k = int(faces)
else:
  k=8

# Outer loop will run till faces / 8
while (i < outer):
    # inner loop will run for each column
    while (j < k):
        # Displaying individual LED
        s.set_pixel(j, i, (0, 255, 0))
        j += 1
        # Checking if row is full then remove 8 from total number of faces and setting inner counter variable value to 0.
        if (j == 8):
            faces -= 8
            # Checking next line contains 8 elements or not. If not then setting k value as remaining faces else k value is 8
            if (int(faces / 8) != 0):
                k = 8
            else:
                k = (faces % 8)
            j = 0
            break
    i += 1
