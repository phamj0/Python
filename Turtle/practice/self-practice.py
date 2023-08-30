
list_of_keys = ['key1', 'key2', 'key3']
list_of_values = [100, 200, 300]

my_dict = {}

for x in range(len(list_of_keys)):
    my_dict[list_of_keys[x]] = list_of_values[x]

print(my_dict.items())

n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:.2f}".format(2**10, n1, n2, n1 * n2)
print(s3)