#Mohtasim Howlader, Aleksandra Koroza: Team Bitelguese
#SoftDev1 pd8
#K16 -- No Trouble
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



DB_FILE="discobandit.db" #delete before every subsequent run

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

with open('courses.csv', newline='') as coursefile:
     coursesDict = csv.DictReader(coursefile)
     createCourses = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"   #build SQL stmt, save as string
     c.execute(createCourses)   #run SQL statement

     #each row is inserted into the courses table, code/mark/id being the column names.
     for row in coursesDict:
         c.execute(f'''INSERT INTO courses (code, mark, id) VALUES("{row['code']}","{ int(row['mark'])}","{int(row['id'])}")''')


with open('peeps.csv', newline='') as peepsfile:
    peepsDict = csv.DictReader(peepsfile)
    createPeeps = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"  #build SQL stmt, save as string
    c.execute(createPeeps)   #run SQL statement

    #each row is inserted into the peeps table, name/age/id being the column names.
    for row in peepsDict:
        c.execute(f'''INSERT INTO peeps(name, age, id) VALUES("{row['name']}","{ int(row['age'])}","{int(row['id'])}")''')





#==========================================================

db.commit() #save changes
db.close()  #close database
