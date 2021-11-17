#Program to find the word frequency in the lsit using "get()"  func

names = ['stephen.marquard', 'louis', 'zqian', 'rjlowe', 'zqian', 'rjlowe', 'cwen', 'cwen', 'gsilver', 'gsilver', 'zqian', 'gsilver', 'wagnermr', 'zqian', 'antranig', 'gopal.ramasammycook', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'stephen.marquard', 'louis', 'louis', 'ray', 'cwen', 'cwen', 'cwen']

count = dict()

for name in names:
    
    # get() will look for key(in here name) and returns the value
    # the 2nd arguement is default value(here 0)

    count[name] = count.get(name,0) + 1     #if gets the name, then add 1 to the value 
                                            #or else assign 0 as value and add 1 

print(count)
