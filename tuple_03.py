fhand = open('words_clean.txt')

#word frequency counting
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#print(counts)
# tmp = sorted(counts.items())
# print(tmp)


#tuple for reversing the key, value pair
tmp = list()
for k,v in counts.items():
    new = (v,k)
    print(new)
    tmp.append(new)

#print(tmp)

new_tmp = sorted(tmp, reverse=True)  #reversily sorted tuple with frequency as the key

print(new_tmp)

# # for v,k in new_tmp:
# #     print(k,v)
