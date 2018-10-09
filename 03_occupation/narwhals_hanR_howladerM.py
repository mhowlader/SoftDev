#Team Narwhals (Robin Han and Mohtasim Howlader)
#SoftDev1 pd8
#K #06: StI/O: Divine your Destiny!
#2018-09-14



file = open("occupations.csv","r")

occupations = {} #dictionary


occList=file.readlines() #list of all of the lines of the csv


for i in range(1, len(occList)-1): #don't want to include first and last line
    line = occList[i] #specific line
    occName = "" #name of occupation
    if line[0] == "\"": #if this line starts with double quotes, do this (the splitting is different)
        quoteSpl=line.split("\"") #split by the double quotes
        occName = quoteSpl[1] #retrive the name of the occupation
        comSpl = line.split(",") #split again, this time by commas
        perc = float(comSpl[len(comSpl)-1]) #get the last element in list because thats the percent
        occupations[occName] = perc #set the key and value in occupation dictionary
    else: #when no quotes in occupation name
        comSpl = line.split(",") # split by comma
        occName = comSpl[0] #the first element is occ name
        perc = float(comSpl[1]) #the second element is the percent
        occupations[occName]=perc #key and value

for x in occupations:
    print (x)
    print (occupations[x])





