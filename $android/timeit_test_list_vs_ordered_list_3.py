import timeit

my_list = list(range(1000000))
my_set = set(my_list)
my_dict = dict.fromkeys(my_list)
print(f"Set membership test time {timeit.timeit(lambda: 1000000000 in my_set)}")
print(f"Dict membership test time {timeit.timeit(lambda: 1000000000 in my_dict)}")
