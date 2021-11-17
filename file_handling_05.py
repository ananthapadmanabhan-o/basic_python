#name of people in email data


fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        pos = line.find(' ')
        spos = line.find('@',pos)
        print(line[pos:spos])


