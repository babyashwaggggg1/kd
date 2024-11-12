print ("hello world")
import random 
from random import randint
health = 100
food = 30
miles = 0
miles = miles + randint(x, y)
define = health - randint(x, y)
define2 = food - randint(x, y)

game = True
print("welcome to jumani, Nigel Billingsley at your service, as you know \njumaji is in great danger,\nthe jaguars eye was stolen by my boss after he sweared that he just wanted to look at it but then one dark night while they were all    asleep I waited for the right moment and I made my move and stole it, now i hand it to you , \nin order to save the game return the jewel to the jaguars eye. The  goal for u,  ill recite in verse.\nReturn the jewel and lift the curse. If you wish to leave the game  you must save jumanji and call out its name. Good luck.")

print("Nigel has left you with the folowing items: \n1. A map \n2. A compass \n3. A flashlight \n4. A knife \n5. A bottle of water \n6 food and water for three days \n7. a gun with 12 bullet and one set of ammo  ")

print("Nigel has dropped u off in the dunes, you need to get to the \ntransportation shed which is 50 miles away, you have to get there by the end of the day. You have to")
while game:
  
  print("player choices")
  print("1.slow pace \n2.fast pace \n3.moderate pace")
  print("4.stop to rest \n5.eat and drink \n6.fill up your water bottle")
  choice=input("enter your choice")
  if choice == "1": 
     print("your health has increased by 5 but you have only traveled 20        miles and you need to get there before the end of the day")
     health = health +5
     miles= miles +randint (10,20)
  if choice == "2":
     print("your health has decreased by 5 but you traveled 40 miles")
     health = health -5
     miles = miles +randint(30,40)
  if choice == "3":
    print ("your health has decreased by 1 but you have traveled 30 miles")
    health = health -1
    miles = miles  +randint (15,25)
  if choice == "4":
    print("you have stopped to rest and your health has increased by 10")
    health = health +10
    miles = miles +0
  if choice == "5":
    print("you have eaten and drunk and your health has increased by 20")
    health = health +20
    miles = miles +0
  if choice == "6":
    print("you have filled up your water bottle but you have traveled 0        miles")
    health = health +0
    miles = miles +0
  if health == 0:
    print("you have died")
    game = False
  if miles >= 200:
    print("you have reached the transportation shed")
    game = False