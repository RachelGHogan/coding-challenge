
players, m = input("Input the number of players followed by the number that determines the order of elimination: ").split(" ")
players = int(players)
m = int(m)
sequence = ""
array = []
x = -1

for i in range (0,players):
    array.append(i)

while len(array) > 0:
    x += 1
    for data in array:
        if (data+1+x)%m == 0:
            sequence+=str(data)+" "
            array.remove(data)

print(sequence)
