# to find most used word and their counts
#using 2 iterable variable with "items()"

fname = 'words.txt'
fhand = open(fname)

#adding word with counts to dictionary
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print(counts)



#finding most used word 
big_count = None
big_word = None
for word,count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = word
print('The most used word in the file "{}" is "{}" and it is used {} times.'.format(fname,big_word,big_count))