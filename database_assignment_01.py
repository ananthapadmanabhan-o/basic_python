import sqlite3 as sq
conn = sq.connect('assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')


fhand = open('mbox.txt')
for line in fhand:
    if not line.startswith('From: '): continue    
    data = line.split()
    ndata = data[1].split('@')
    org = ndata[1]
    
    cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    
    row = cur.fetchone()

    if row == None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?',(org,))
   
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'  
for row in cur.execute(sqlstr):
    print(row[0],row[1])


cur.close()

