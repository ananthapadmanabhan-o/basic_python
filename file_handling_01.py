#words.txt

fopen = open('words.txt')

for line in fopen:
    print(line.rstrip())
    