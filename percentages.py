from collections import OrderedDict
import re


###read file and turn contents into a string
file  = open("words.txt", "r")
x = file.read()
file.close()

###load all chars into characters
characters = {"whitespace": 0, "symbols": 0}
i = 0



###loop through string made from the text file
while(i < len(x)) :
    ###check if the char in the string is already in the character dictionary
    if(x[i] in characters) :
        ###if char already exist, increase it's value
        #print(type(x[i]))
        characters[x[i]] = characters[x[i]]+1
        i = i+1
    #TODO: check for special blank characters like return, tab, newline and put as one symbol (doesn't work)
    #TODO: combine symbol to one char
    elif (x[i] == '') :
        print("EMPTY SPACE")
        characters["whitespace"] += 1
        i = i+1
    ###not working!
    elif (x[i] == '\t') :
        print("TAB")
        characters["whitespace"] += 1
        i = i+1
    elif (x[i] == ' ') :
        print("SPACE")
        characters["whitespace"] += 1
        i = i+1
    elif (x[i] == '\n') :
        print("NEW LINE")
        characters["whitespace"] += 1
        i = i+1
    ###using regex to find all symbols
    elif(re.findall('[^A-Za-z0-9]', x[i])) :
        characters["symbols"] += 1
        i = i+1
    ###if not in dictionary already
    else :
        characters[x[i]] = 1
        i = i+1


###get probability of each letter from character
percents = {}
i = 0
for k in characters :
    #move key to new charactersonary
    percents[k] = k
    percent = round((characters[k]/len(x))*100, 2)
    percents[k] = percent
    i = i+1

for l in percents :
    print(l, percents[l])

def getPercentages() :
    for w in percents :
        print(w, percents[w])
    return percents
    
numStr = 1
###recalculating new dictionary based on input given
def recalculatePercentages(numStr) :
    #if numStr == None : 1
    ###we want numStr's pie slices and the rest are others

    others = len(percents) - numStr

    ###order the dictionary
    orderedDict = {}
    orderedDict = OrderedDict()
    for percent in percents :
        orderedDict[percent] = percents[percent]


    print("ITS STILL NOT ORDERED")
    for order in orderedDict :
        ###setting the key to counter of numbers and value to ordered dict's values but should be keys
        print(order, orderedDict[order])


    ###index dict holds key: counter, value: key from old dict
    indexDicts = {}
    counter = 0
    for order in orderedDict :
        ###setting the key to counter of numbers and value to ordered dict's values but should be keys
        indexDicts[counter] = order
        counter += 1


    ###how to delete by value
    for blah in range(others):
        print(blah, indexDicts[blah])
        del orderedDict[indexDicts[blah]]

    ###summing the percentages of relevant pie slices to find irrelevant pie slice percentage
    sum = 0
    for order in orderedDict :
        sum += orderedDict[order]
    otherPercent = 100-sum
    orderedDict["others"] = otherPercent

    return orderedDict

recalculatePercentages(numStr)
