
#list of name
names = ['ananthan','nandu','stephen.marquard', 'louis', 'zqian', 'rjlowe', 'zqian', 'rjlowe', 'cwen', 'cwen', 'gsilver', 'gsilver', 'zqian', 'gsilver', 'wagnermr', 'zqian', 'antranig', 'gopal.ramasammycook', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'david.horwitz', 'stephen.marquard', 'louis', 'louis', 'ray', 'cwen', 'cwen', 'cwen']

#frequency of word occurence
count={'stephen.marquard': 2, 'louis': 3, 'zqian': 4, 'rjlowe': 2, 'cwen': 5, 'gsilver': 3, 'wagnermr': 1, 'antranig': 1, 'gopal.ramasammycook': 1, 'david.horwitz': 4, 'ray': 1}

for name in names:
    # if name in count:
    #     x=count[name]
    # else:
    #     x=0
    x = count.get(name,0)          #above commented line of code is replaced using single line with get()
    print("{}: {}".format(name,x))
