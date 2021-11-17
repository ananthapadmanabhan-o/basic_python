#!/usr/bin/python3

length = input("Enter the length: ")         
breadth = input("Enter the breadth: ")



#converstion of string type to float

try:                                         # try will tries to run the operation in case of an error
    f_length = float(length) 
    f_breadth = float(breadth)
except:                                      # except runs operation if command under try show error                        
    print("Please enter a number.......")
    quit()                                   # quit from the program and do not run the prgrm further

area = f_length*f_breadth                        
print("The area of the retangle is",area)