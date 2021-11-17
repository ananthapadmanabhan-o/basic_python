
#X-DSPAM-Processed: Thu Jan  3 16:29:07 2008
#printing line wich starts with x-pam~~~

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Processed:'):
        print(line)

        

