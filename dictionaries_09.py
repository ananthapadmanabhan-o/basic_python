count={'stephen.marquard': 2, 'louis': 3, 'zqian': 4, 'rjlowe': 2, 'cwen': 5}

#Two variable iteratin in for loop using items()

print('\n')
print(count.items())

print('\n')
for item in count.items():              #Returns key & value as a pair in tuple
    print(item)

print('\n')

for keey,vaalue in count.items():         #Returns key & value with 2 iterable variable
    print(keey,vaalue)

print('\n')


for keey,value in count.items():         #Returns only key
    print(keey)

print('\n')

for keey,vaalue in count.items():         #Returns only value
    print(vaalue)
