file  = open("words.txt", "r")

#read file and turn contents into a string
x = file.read()

#load all chars into dictionary
dicti = {}
i = 0
while(i < len(x)) :
    if(x[i] in dicti) :
        dicti[x[i]] = dicti[x[i]]+1
        i = i+1
    #TODO: check for special blank characters like return, tab, newline (doesn't work)
    if (x[i] == type('\t')) :
        dicti[x[i]] = "newtab"
        i = i+1
    if (x[i] == type('\n')) :
        dicti[x[i]] = "new line"
        i = i+1
    else :
        dicti[x[i]] = 1
        i = i+1


# for j in dicti:
#     print(j, " ", dicti[j])


#get probability of each letter from dictionary
dict2 = {}
i = 0
for k in dicti :
    #move key to new dictionary
    dict2[k] = k
    percent = (dicti[k]/len(x))*100
    dict2[k] = percent
    i = i+1

for l in dict2 :
    print(l, " ", dict2[l])
