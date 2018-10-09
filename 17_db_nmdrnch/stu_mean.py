#Team Watch_Out_For_Snakes (Joan Chirinos, Mohtasim Howlader)
#SoftDev1 pd8
#K17 -- Average
#2019-10-09


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

# adds a row to the courses table based on the given parameters
def add_course_row(code, mark, id):
    c.execute('INSERT INTO courses VALUES({}, {}, {})'.format(course, mark, id))

def go():
    c.execute('CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, avg INTEGER)') #Create the peeps_avg table with two columns: ID as primary key, and avg for average

    l = c.execute('SELECT peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id') #l is set to an iterable cursor object with peep id that match courses id, and the corresponding mark for that course
    d = {} #dictionary

    for i in l: #
        if i[0] in d: #checks if the id is already in the dictionary d
            d[i[0]] += [i[1]] # if it is, add the mark to the values already there
        else:
            d[i[0]] = [i[1]] #if not, create a new key for the dictionary, and set its value to i[1] which is the mark

    for i in d: #for each person
        avg = sum(d[i]) / len(d[i]) #calculate average for each person by adding all of the marks and dividing by number of marks
        c.execute('INSERT INTO peeps_avg VALUES({}, {})'.format(i, avg)) #populate table peeps_avg

    db.commit()

    x = c.execute('SELECT peeps.name, peeps.id, avg FROM peeps_avg, peeps WHERE peeps.id = peeps_avg.id')
    for i in x: #iterable table created in previous execute
        print('name: {}\n\tid: {}\n\tavg: {}\n'.format(i[0], i[1], i[2])) #print student name, id, and average

    db.close()

go()
