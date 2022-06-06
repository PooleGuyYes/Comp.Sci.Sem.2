import sys
import random

foods_0 = ["Noodles", "Soda", "Sushi", "Anime"]
foods_1 = ["Fried Chicken", "Cheeseburger", "Sandwich", "Steak"]
foods_2 = ["Ramen", "Fried Rice", "Sushi", "Anime"]
foods_3 = ["ART KIM", "NAT HWAG", "LIAM", "CHRIS"]
x = random.randrange(0,3)
if x == 0:
    print("======================================================")
    print(" ")
    print("===== NAT HWAG UNOFFICIAL RESTRAUNT FOR BAD FOOD =====")
    print(" ")
    print("======================================================")
elif x == 1:
    print("======================================================")
    print(" ")
    print("======== RORDAN GRAMSEY SUCKY STORE FOR KIDS ========")
    print(" ")
    print("======================================================")
elif x == 2:
    print("======================================================")
    print(" ")
    print("================== SUSSY BAKA TOWN ==================")
    print(" ")
    print("======================================================")
elif x == 3:
    print("======================================================")
    print(" ")
    print("======== COLLABERATION SUSSY PLACE FOR FOOD ========")
    print(" ")
    print("======================================================")
print(" ")
start = (input("Would you like to see the menu? (y/n) "))
print(" ")
if start == 'y':
    print(" ")
    print("======================================================")
    print(" ")
elif start == 'n':
    print(" ")
    print("======================================================")
    sys.exit()
else:
    print(" ")
    print("======================================================")
    sys.exit()
print("MENU: ")
print(" ")
if x == 0:
    print(foods_0[0])
    print(" ")
    print(foods_0[1])
    print(" ")
    print(foods_0[2])
    print(" ")
    print(foods_0[3])
    print(" ")
elif x == 1:
    print(foods_1[0])
    print(" ")
    print(foods_1[1])
    print(" ")
    print(foods_1[2])
    print(" ")
    print(foods_1[3])
    print(" ")
elif x == 2:
    print(foods_2[0])
    print(" ")
    print(foods_2[1])
    print(" ")
    print(foods_2[2])
    print(" ")
    print(foods_2[3])
    print(" ")
elif x == 3:
    print(foods_3[0])
    print(" ")
    print(foods_3[1])
    print(" ")
    print(foods_3[2])
    print(" ")
    print(foods_3[3])
    print(" ")
print("======================================================")
print(" ")
choice = int(input("What would you like to get? (1,2,3,4) "))
print(" ")
if choice == 1:
    if x == 0:
        print("You ordered a")
        print(" ")
        print(foods_0[0])
    elif x == 1:
        print("You ordered a")
        print(" ")
        print(foods_1[0])
    elif x == 2:
        print("You ordered a")
        print(" ")
        print(foods_2[0])
    elif x == 3:
        print("You ordered a")
        print(" ")
        print(foods_3[0])
elif choice == 2:
    if x == 0:
        print("You ordered a")
        print(" ")
        print(foods_0[1])
    elif x == 1:
        print("You ordered a")
        print(" ")
        print(foods_1[1])
    elif x == 2:
        print("You ordered a")
        print(" ")
        print(foods_2[1])
    elif x == 3:
        print("You ordered a")
        print(" ")
        print(foods_3[1])
elif choice == 3:
    if x == 0:
        print("You ordered a")
        print(" ")
        print(foods_0[2])
    elif x == 1:
        print("You ordered a")
        print(" ")
        print(foods_1[2])
    elif x == 2:
        print("You ordered a")
        print(" ")
        print(foods_2[2])
    elif x == 3:
        print("You ordered a")
        print(" ")
        print(foods_3[2])
elif choice == 4:
    if x == 0:
        print("You ordered a")
        print(foods_0[3])
    elif x == 1:
        print("You ordered a")
        print(" ")
        print(foods_1[3])
    elif x == 2:
        print("You ordered a")
        print(" ")
        print(foods_2[3])
    elif x == 3:
        print("You ordered a")
        print(" ")
        print(foods_3[3])
else:
    print("That was not on the menu, goodbye.")
    print(" ")
    print("======================================================")
    sys.exit()
print(" ")
print("======================================================")
print("Thank You for Dining!")
print("======================================================")
