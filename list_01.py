#storing random numbers in list and sorting

import random

number = list()

for i in range(100):
    num = random.randint(0,200)
    number.append(num)

#number.sort()


y = number
x = sorted(number)
print(y)
print('\n\n',x)

