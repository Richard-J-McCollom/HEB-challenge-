list1 = {}
key = []
f = open("input.txt", "r")
out = open("output.txt", "w")
length = 0
for line in f:
    for word in line.split():                             #split line by spaces to get our words
        if any(letter.isalpha() for letter in word):      #make sure there is at least 1 letter 
            while not word[-1].isalpha():
                word = word[:-1]                          #while the back of the word contains punctuation trim the last character off
            while not word[0].isalpha():
                word = word[1:]                           #while the front of the word contains punctuation trim the first character off
            word = word.lower()                           #ignore case
            if len(word) > length:   
                length = len(word)                        #find the longest name so we can format our output later
            if word in key:
                list1[word] += 1
            else:
                list1[word] = 1
                key.append(word)          
                                                          #dictionary is complete {words,occurences}
wantedVal = 0
for values in list1.values():
    if values > wantedVal:
        wantedVal = values                                #get largest value for printing order
end = 1                                   
spacesNeeded = 0
while end < len(key):                                     #dont exit untill we have printed all the names in the key
    for name in key:                                  
        formatted = ""
        if list1[name] == wantedVal:                      #print all names in the key with highest value, then highest-1, and so on
            spacesNeeded = length - len(name)             #find number of spaces needed to format
            i = 0
            while i < spacesNeeded:
                formatted = formatted + " "
                i += 1                                    #add formatting spaces so that all names are the same length
            print(formatted + name + " | ", end = ' ', file = out)
            i = 0
            while i < wantedVal:
                print("=", end = '', file = out)
                i += 1                                    #get same number of = as the count the name has
            print( " (" + str(wantedVal) + ")", file = out)
            end += 1
    wantedVal -= 1
out.close()                                               
f.close()                                                 #close our input and output files