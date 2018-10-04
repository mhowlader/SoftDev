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
     courseRead = csv.DictReader(coursefile)

with open('peeps.csv', newline='') as peepsfile:
    peepsRead = csv.DictReader(peepsfile)


    

     


command = "CREATE TABLE roster(name TEXT, userid INTEGER)"+"INSERT INTO roster VALUES('drums',0)"         #build SQL stmt, save as string
c.execute(command)   #run SQL statement
#==========================================================

db.commit() #save changes
db.close()  #close database


