#Program to find the word frequency

count = dict()

# list of names with repeating names
names = ['stephen.marquard', 'louis', 'zqian', 'rjlowe', 'zqian', 'rjlowe', 'cwen', 'cwen', 'gsilver', 'gsilver', 'zqian', 'gsilver', 'wagnermr', 'zqian', 'antranig', 'gopal.ramasammycook', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'stephen.marquard', 'louis', 'louis', 'ray', 'cwen', 'cwen', 'cwen']

for name in names:                      #loops through each name in the list
    if name not in count:               #if name is not counted it'll assign 1
        count[name] = 1                 
    else:
        count[name] += 1                #if the name is counted it'll add 1 in each time if counting                

print(count)
