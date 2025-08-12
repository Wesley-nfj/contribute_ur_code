import random
from collections import defaultdict

def roll_dice():
    return random.randint(1,6)
    
#Stores how many times a face appears
face_count= defaultdict(int)

total_roll =0

#Ask user for input
while True:
   user_input= input("\n Roll a dice? (yes or no):\n")
    
   if user_input== "yes":
      result= roll_dice()
      face_count[result] += 1 #Adds 1 to the count of your result (face)
      total_roll +=1 
      print(f"You rolled a {result}")

   elif user_input== "no":
       #provides the game summary
       print("\n🎯 Roll Summary:")
       print(f"Total rolls: {total_roll}")

       #Shows how many times each face came up
       for face in range(1, 7):
           count = face_count[face]
           print(f"Face {face}: {count}")
           print("BYE!")
       break

   else:
    print("Enter yes or no")
    continue