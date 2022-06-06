import random
print("=============================================")
print("=== NAT HWAG UNOFFICIAL NUMBER RANDOMIZER ===")
print("=============================================")
print(" ")
choice = int(input("Choose how many numbers you want: "))
print(" ")
print("=============================================")
print(" ")
thislist = [1,2,3,4,5,6,7,8,9,10]
for i in range (0,choice):
    random.choice(thislist)
    print(thislist[0])
    print(" ")
print("=============================================")