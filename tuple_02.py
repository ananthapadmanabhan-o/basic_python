#sorting in tuple

data = {'b':47,'c':9,'a':45}   #unsorted data

new_data = data.items()        # data ======>>>>> list of tuples

print(new_data)


for k,v in sorted(new_data):
    print(k,v)