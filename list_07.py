#print the name and not print name which is already printed 

names = ['stephen.marquard', 'louis', 'zqian', 'rjlowe', 'zqian', 'rjlowe', 'cwen', 'cwen', 'gsilver', 'gsilver', 'zqian', 'gsilver', 'wagnermr', 'zqian', 'antranig', 'gopal.ramasammycook', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'stephen.marquard', 'louis', 'louis', 'ray', 'cwen', 'cwen', 'cwen']
already_printed = list()

for name in names:
    if name not in already_printed:     #checking the name if already printed
                                        #if the number is not in already printed list then it'll print                                   
        print(name)                     #if name is in "already_printed" list it'll ignore
        already_printed.append(name)    #add the printed name in "already_printed" list
            
    