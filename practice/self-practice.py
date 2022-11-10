
list_of_keys = ['key1', 'key2', 'key3']
list_of_values = [100, 200, 300]

my_dict = {}

for x in list_of_keys:
    for y in list_of_values:
        my_dict[x] = y

print(my_dict.items())
