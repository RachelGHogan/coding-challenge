testCases = int(input("Input the number of test cases: "))
n = " "
k = " "
maxMod = 0
array = []

for i in range (testCases):
    n, k = input("Input the number of coins followed by the max amount of people: ").split(" ")
    n = int(n)
    k = int(k)
    array.append([n,k])
    
for data in array:
    maxMod = 0
    n = array[array.index(data)][0]
    k = array[array.index(data)][1]
    for i in range(1,k+1):
        if n%i > maxMod:
            maxMod = n%i
    print(maxMod)
