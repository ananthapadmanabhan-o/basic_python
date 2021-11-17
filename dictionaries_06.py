# program to find word frequency in a file or a text
words = list()
count = dict()

fhand = open('words_clean.txt')
#making of words list
for line in fhand:
    line = line.rstrip()
    data = line.split()
    for item in data:
        words.append(item)

#print(words)

for word in words:
    count[word] = count.get(word,0) + 1

print(count)