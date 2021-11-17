# finding number from a string
#storing number to a list
#calculating the total sum using "sum()" function



                                                #  BUILT IN FUNCTIONS FOR LIST  



fhand = open('mbox-short.txt')


#X-DSPAM-Confidence: 0.6959


number_list = list()

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        data = line.split()
        
        #['X-DSPAM-Confidence', ' 0.6959']

        number = data[1]

        f_number = float(number)

        number_list.append(f_number)

#  BUILT IN FUNCTIONS FOR LIST  

sorted_list = sorted(number_list)
sum_list = sum(sorted_list)
small_num = min(sorted_list)
large_num = max(sorted_list)

print(sorted_list)
print('\nThe sum of tortal numbers =',sum_list)
print('\nThe smallest number in the list is {} and largest is {}'.format(small_num,large_num))

      

      

        

