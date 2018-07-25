
testCases = int(input("Input the number of testcases: "))
Rs = 0
array = []
num = 0

for i in range(testCases):
    Rs = int(input("please input an amount of Rs: "))
    array.append(Rs)
    
for data in array:
    num = 0
    while data-100 >= 0:
        data-=100
        num += 1
    while data-50 >= 0:
        data-=50
        num += 1
    while data-10 >= 0:
        data-=10
        num += 1
    while data-5 >= 0:
        data-=5
        num += 1
    while data-2 >= 0:
        data-=2
        num += 1
    while data-1 >= 0:
        data-=1
        num += 1
    print(num)
