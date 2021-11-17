#  format of string
# From gsilver@umich.edu Fri Jan  4 11:10:22 2008

fhand = open('mbox-short.txt')
data = list()
name_lst = list()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        if line.startswith('From: '):
            continue

        pos = line.find(' ')
        spos = line.find('@',pos)
        data.append(line[pos:spos])

for name in data:
    if name in name_lst:
        continue
    name_lst.append(name)


for name in name_lst:
    print(name)
