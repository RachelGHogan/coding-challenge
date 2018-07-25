testCases = int(input("Input the number of test cases: "))
cupCakes = 0
array = []
size = 0

for i in range (testCases):
    array.append(int(input("Input the number of cupcakes: ")))
    

for data in array:
    size = 0
    for i in range(1, data+1):
        if data%i >= cupCakes:
            cupCakes = data%i
            size = i
    print(size)
        
