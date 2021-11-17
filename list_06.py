#   GAURDIAN STATMENT   

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    wds = line.split()
   
    # Gaurdian in compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
        
    #print(wds)
    print(wds[2])
    
    