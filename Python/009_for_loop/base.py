print("||| NAT HWAG UNOFFICIAL LINE GENERATOR FOR NOOBS |||")
print(" ")
print("============================================")
print(" ")
size = int(input("ENTER A LINE SIZE: "))
print(" ")
vh = input("VERTICLE OR HORIZONTAL LINE (v/h): ")
print(" ")
print("============================================")
print(" ")
for i in range (0,size):
    if vh == "v":
        print("*")
    elif vh == "h":
        print("*", end = (" "))