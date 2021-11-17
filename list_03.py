# storing line in list using split
# print the part using index

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        lst = line.split()
        
        
        #['From', 'zqian@umich.edu', 'Fri', 'Jan', '4', '16:10:39', '2008']

        print(lst[5])