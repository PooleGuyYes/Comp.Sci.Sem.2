print("==============================")
print("=== NAT HWAG WHALE COUNTER ===")
print("==============================")
print(" ")
sentence = "whale, hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
print(sentence)
print(" ")
print("==============================")
print(" ")
count = 0
for i in range(0,len(sentence)):
    if(sentence[i:i+5] == "whale"):
        count = count + 1
print(count)
print(" ")
print("==============================")













#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
