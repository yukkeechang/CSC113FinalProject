file  = open("words.txt", "r")

#read file and turn contents into a string
x = file.read()

#load all chars into charactersonary
characters = {}
i = 0
while(i < len(x)) :
    if(x[i] in characters) :
        characters[x[i]] = characters[x[i]]+1
        i = i+1
    #TODO: check for special blank characters like return, tab, newline (doesn't work)
    #TODO: get number input from part a then make the others group
    if (x[i] == type('\t')) :
        characters[x[i]] = "newtab"
        i = i+1
    if (x[i] == type('\n')) :
        characters[x[i]] = "new line"
        i = i+1
    else :
        characters[x[i]] = 1
        i = i+1


# for j in characters:
#     print(j, " ", characters[j])


#get probability of each letter from charactersonary
dict2 = {}
i = 0
for k in characters :
    #move key to new charactersonary
    dict2[k] = k
    percent = round((characters[k]/len(x))*100, 2)
    dict2[k] = percent
    i = i+1

for l in dict2 :
    print(l, " ", dict2[l])
