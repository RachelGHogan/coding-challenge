t = int(input("input number of test cases: "))
x = 0
i = 0
j = 1
num = 0

for c in range (t):
    n,d = input("input n and d: ").split(" ")
    n = int(n)
    d = int(d)
    for x in range (1,n+1):
        i += 1
        j = i+1
        for y in range (i,n+1):
            j += 1
            print(j)
            if j%d == 0 and i%d == 0:
                 num += 1
    print(num)

            
        
