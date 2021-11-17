'''The Equality operator (==) compares the values of both the operands and checks for value equality. 
Whereas the ‘is’ operator checks whether both the operands refer to the same object or not.
'''
''' python3 code to illustrate the difference between == and is operator, [] is an empty list'''


list1 = []
list2 = []
list3=list1
'''
print(type(list1))
print(type(list2))
print(type(list3))
'''
if (list1 == list2):
	print("list1 == list2\n")
else:
	print("list1 != list2\n")

if (list1 == list3):
    	print("list1 == list3\n")
else:
	print("list1 != list3\n")

if (list1 is list2):
	print("list1 is list2\n")
else:
	print("list1 is not list2\n")

if (list1 is list3):
	print("list1 is list3\n")
else:
	print("list1 is not list3\n")

list3 = list3 + list2
'''
print(type(list1))
print(type(list2))
print(type(list3))

'''
if (list1 is list3):
	print("list1 is list3\n")
else:
	print("list1 is not list3\n")

if (list1 == list3):
    	print("list1 == list3\n")
else:
	print("list1 != list3\n")
