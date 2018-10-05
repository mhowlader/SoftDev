#Mohtasim Howlader, Aleksandra Koroza
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('courses.csv', newline='') as coursefile:
     courseDict = csv.DictReader(coursefile)

with open('peeps.csv', newline='') as peepsfile:
    peepsDict = csv.DictReader(peepsfile)
    createPeeps = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"         #build SQL stmt, save as string
    c.execute(createPeeps)   #run SQL statement
    for row in peepsDict:
        c.execute(f'''INSERT INTO peeps (name, age, id) VALUES("{row['name']}","{ int(row['age'])}","{int(row['id'])}")''')
        #c.execute("INSERT INTO peeps (name, age, id) VALUES ('hello', 5, 6)")


# createPeeps = "CREATE TABLE IF NOT EXISTS peeps(name TEXT, age INTEGER, id INTEGER)"         #build SQL stmt, save as string
# c.execute(createPeeps)   #run SQL statement
# for key, value in peepsDict.items():
#     for obj in value:
#         c.execute(f'INSERT INTO peeps VALUES({key}, {obj}')




#==========================================================

db.commit() #save changes
db.close()  #close database
