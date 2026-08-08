# my_list = [1, 2, 5]

# def my_function(e):
#     return e * e

# print(list(map(my_function, my_list)))

# new_list = [] 
# for i in range(len(my_list)):
#     new_list.append(my_function(my_list[i]))

#     print(new_list)

# from functools import reduce
# my_list = [1, 2, 5]

# def my_filt_func(a,b):
#     reduce = a - b
# print(reduce(my_filt_func,my_list[i]))

my_list = [1, 2, 5]

def mu_function(my_list_item):
    return my_list_item * my_list_item

my_map_object = map(lambda e:e*e, my_list)

print()