#Team moBin -- Robin Han & Mohtasim Howlader
#SoftDev1 pd08
#K06 -- Stl/O: Divine your Destiny!
#2018-09-13

import csv
import random

#returns random occupation based on percent of likelihood
def chooseOccupation(d,totalSum):
        #variable to match occupation with its respective weight
        i = 0
        occ = d.keys()
        weights = d.values()
        # generating a random number float from 0 to the total sum of the weights
        #print (totalSum)
        randWeight = float(random.randrange(0,totalSum*100))/100
        #print (randWeight)
        i = -1
        for weight in weights:
                #choosing the occupation if the randWeight created lies between the range of its weight.

                randWeight -= weight
                if randWeight <= 0:
                        break
                i+=1
                #print(i)


        #print (i)
        #print (len(list(weights)))
        return list(occ)[i]

def main():
        # initialize dictionary

        d = {} #the final dictionary
        with open('occupations.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                # eliminates first row of csv file
                next(reader)
                # loops through each row of csv file
                for row in reader:
                        # checks to see that the total isn't added to the dictionary
                        #print (row['Job Class'])
                        if row['Job Class'] != "Total":
                               d[row['Job Class']] = float(row['Percentage'])
                        else:
                                totalSum = float(row['Percentage'])
        print(chooseOccupation(d,totalSum))

        #testing
        margin = 15
        testDict = {}
        total = 100000
        for i in range(0,total):
                occ = chooseOccupation(d,totalSum)
                #print (occ)
                if (occ not in testDict.keys()):
                        testDict[occ] = 1
                else:
                        testDict[occ] +=1
        #print (testDict)
        wrongAns = False
        for occupation in testDict.keys():
                #print (d.get(occupation))
                #print (d.get(occupation) + margin)
                if not ((testDict.get(occupation) * 100 / total <= (d.get(occupation)+margin)* 100 /totalSum) and (testDict.get(occupation) * 100 / total >= (d.get(occupation) - margin)) * 100 /totalSum):
                        #print (testDict.get(occupation) * 100 / total)
                        #print ((d.get(occupation)+margin) * 100 /totalSum)
                        #print ((d.get(occupation)-margin) * 100 /totalSum)
                        print ("Check the " + occupation + " occupation")
                        print ("You may want to recheck your solution...")
                        wrongAns = True
                        break;
        if not (wrongAns):
                print ("PASSED!")


main()
