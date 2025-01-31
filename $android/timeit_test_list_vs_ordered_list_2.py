from tqdm import tqdm
import timeit

def time_list_membership(my_list, target):
    start_time = timeit.default_timer()
    for _ in tqdm(range(1000), desc="List Membership Test"):
        target in my_list
    end_time = timeit.default_timer()
    return end_time - start_time

def time_set_membership(my_set, target):
    start_time = timeit.default_timer()
    for _ in tqdm(range(1000), desc="Set Membership Test"):
        target in my_set
    end_time = timeit.default_timer()
    return end_time - start_time

# Create a large list and set
my_list = list(range(1000000))
my_set = set(range(1000000))
target_value = 1000000

# Time membership testing for list
list_time = time_list_membership(my_list, target_value)

# Time membership testing for set
set_time = time_set_membership(my_set, target_value)

print(f"List membership test time: {list_time:.6f} seconds")
print(f"Set membership test time: {set_time:.6f} seconds")