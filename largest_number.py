'''Random list operation with 'Functions' and "For" loop'''

import random

random_lst=[]


def generate_random_lst(size,first,last):
    for i in range(size):
        num = random.randint(first,last)
        random_lst.append(num)
    return random_lst


def largest_num(random_lst):
    large = random_lst[0]

    for i in random_lst:
        if i > large:
            large = i
    return large

def sum_list(random_lst):
    sum = 0
    for value in random_lst:
        sum+=value
    return sum


size = int(input("Enter the size of the list: "))
begin = int(input("Enter the begining of range: "))
end = int(input("Enter the ending of range: "))

lst = generate_random_lst(size,begin,end)
large = largest_num(lst)
sum = sum_list(lst)


print("\nThe list is {}\nThe largest number in the list is {}\nThe sum of the total number is {}".format(lst,large,sum))