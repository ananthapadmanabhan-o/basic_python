import sqlite3 as sq

conn = sq.connect('email.sqlite')       #makes a database file 
cur = conn.cursor()  


#helpful when the code is run multiple times from getting Error: (table counts already exists)
cur.execute('DROP TABLE IF EXISTS counts') #will drop down the table if already exits

#creates New table called counts with column named email and count
cur.execute('CREATE TABLE counts(email TEXT, count INTEGER)')

#collects the email from the txt file and stores it in the database
fhand = open('mbox.txt')

for line in fhand:
    if not line.startswith('From'): continue    
    line = line.split()
    email = line[1]                     #parses extracts the email from the line
    cur.execute('SELECT count FROM counts WHERE email = ?',(email,))  #select the count with "email" as an arguement
                                                                      # " ? " symbol prevents sql injection     
                                                                      #arguement in the format of tuple
    
    row = cur.fetchone() #fetches the data
    
    #checks for the existense email in the database
    #if not then adds email to db and gives count = 1 
    #if already exists then count of the email is updated by value 1
    if row == None:
        cur.execute('INSERT INTO counts (email,count) VALUES(?,1)',(email,))
    else: 
        cur.execute('UPDATE counts SET count = count +1 WHERE email = ?',(email,))

conn.commit()  #writing the db to the disk


#for displaying the data
sqlstr = 'SELECT email, count FROM counts ORDER BY count DESC LIMIT 10'  

for row in cur.execute(sqlstr):
    print(row[0],row[1])

cur.close()