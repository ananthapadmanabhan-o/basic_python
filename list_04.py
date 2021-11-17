# extracting name using double split
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        #From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
       
        word = line.split()
        
        #['From', 'david.horwitz@uct.ac.za', 'Fri', 'Jan', '4', '07:02:32', '2008']
       
        email = word[1]

        #david.horwitz@uct.ac.za

        data = email.split('@')

        #['david.horwitz', 'uct.ac.za']

        name = data[0]

        print(name)


        

