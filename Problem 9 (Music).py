testCases = int(input("Input the number of words to find frequencies of: "))
array = []
lyrics = []
occurance = 0
result = 0

for i in range (testCases):
    array.append(input("Input the word: "))

num = int(input("Input the number of lyrics to add to the index: "))

for i in range (num):
    lyrics.append(input("Input the lyric: "))

for data in array:
    lastFound = 0
    occurance = 0
    for i in range (len(lyrics)):
        lastFound = 0
        
        while lyrics[i].find(data,lastFound, len(lyrics[i])) != -1:
            
            result = lyrics[i].find(data,lastFound, len(lyrics[i]))
            
            if (result != -1):
                lastFound = result+1
                occurance += 1
                
    print(occurance)
                        
        
