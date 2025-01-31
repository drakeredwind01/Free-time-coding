import timeit

# Create a large list and set
my_list = list(range(1000000))
my_set = set(my_list)

# Time membership testing for list
list_time = timeit.timeit(lambda: 1000000 in my_list)

# Time membership testing for set
set_time = timeit.timeit(lambda: 1000000 in my_set)

print(f"List membership test time: {list_time:.6f} seconds")
print(f"Set membership test time: {set_time:.6f} seconds")